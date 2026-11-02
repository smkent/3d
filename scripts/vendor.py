# /// script
# requires-python = ">=3.11"
# ///
"""Download third-party site assets listed in vendor.toml.

Files are downloaded when either vendor.toml is changed or any referenced files
are absent.

Replace this with Zensical native `privacy` plugin support when available:
https://github.com/zensical/backlog/issues/35
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tomllib
import urllib.request
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urlsplit

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence
    from typing import Any

MANIFEST = Path("vendor.toml")
DEST = Path("docs/vendor")
USER_AGENT = "3d-vendor (+https://github.com/smkent/3d)"
STATE_FILE = ".vendor.json"
FONTS_CSS = "fonts/fonts.css"
FONTSOURCE_URL = "https://cdn.jsdelivr.net/npm/@fontsource/{name}@{version}"
FONT_FACE_RE = re.compile(
    r"/\* (?P<id>\S+) \*/\s*(?P<rule>@font-face \{.*?\})", re.DOTALL
)
FONT_SRC_RE = re.compile(r"src: [^;]+;")
FONT_WOFF2_RE = re.compile(r"url\(\./files/([^)]+\.woff2)\)")
FONT_FAMILY_RE = re.compile(r"font-family: '([^']+)';")


@dataclass
class VendorAssets:
    dest: Path = field(default_factory=lambda: Path("docs/vendor"))

    @cached_property
    def args(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
        parser.add_argument(
            "-f",
            "--force",
            action="store_true",
            help="Download files even if already present",
        )
        return parser.parse_args()

    def save_file(self, data: bytes, path: str) -> None:
        target = DEST / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def __call__(self) -> None:
        manifest_data = MANIFEST.read_bytes()
        manifest_key = hashlib.sha256(manifest_data).hexdigest()
        state_file = DEST / STATE_FILE
        try:
            state = json.loads(state_file.read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            state = {}
        if (
            not self.args.force
            and state.get("sha256sum") == manifest_key
            and all((DEST / path).is_file() for path in state.get("files", []))
        ):
            print(f"{DEST} is up to date")
            return

        manifest = tomllib.loads(manifest_data.decode())
        downloads = dict(manifest.get("files", {}))
        downloads |= {
            self.external_path(url): url
            for url in manifest.get("external", {}).get("urls", [])
        }
        files: set[str] = set()
        if "fonts" in manifest:
            font_downloads, fonts_css = self.vendor_fonts(manifest["fonts"])
            downloads |= font_downloads
            files.add(FONTS_CSS)
            self.save_file(fonts_css.encode(), FONTS_CSS)
        for path, url in sorted(downloads.items()):
            print(f"Downloading {url}")
            files.add(path)
            self.save_file(self.fetch(url), path)
        self.prune(DEST, {*files, STATE_FILE})
        state_file.write_text(
            json.dumps(
                {"sha256sum": manifest_key, "files": sorted(files)}, indent=2
            )
        )
        print(f"Vendored {len(files)} files to {DEST}")

    def fetch(self, url: str) -> bytes:
        if urlsplit(url).scheme != "https":
            raise ValueError(f"Only https URLs are supported: {url}")
        # Some hosts reject urllib's default user agent
        request = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT}
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read()

    def external_path(self, url: str) -> str:
        """Return the vendored path for an external URL."""
        parts = urlsplit(url)
        return f"external/{parts.netloc}{parts.path}"

    def font_faces(
        self, css: str, name: str, subsets: Sequence[str]
    ) -> Iterator[tuple[str, str, str]]:
        """Yield (family, woff2 file, rule) for Fontsource rules in subsets."""
        for match in FONT_FACE_RE.finditer(css):
            # Rule IDs are formatted as <name>-<subset>-<weight>-<style>
            subset = match["id"].rsplit("-", 2)[0].removeprefix(f"{name}-")
            if subset not in subsets:
                continue
            rule = match["rule"]
            family = FONT_FAMILY_RE.search(rule)
            woff2 = FONT_WOFF2_RE.search(rule)
            if not family or not woff2:
                raise ValueError(
                    f"Unexpected Fontsource rule format: {match['id']}"
                )
            rule = FONT_SRC_RE.sub(
                f"src: url({woff2[1]}) format('woff2');", rule
            )
            yield family[1], woff2[1], rule

    def vendor_fonts(
        self, config: dict[str, Any]
    ) -> tuple[dict[str, str], str]:
        """Return font file downloads and the generated fonts.css."""
        downloads: dict[str, str] = {}
        css = [
            f"/* Fontsource {config['version']} (https://fontsource.org) */\n"
        ]
        variables = []
        for role in ("text", "code"):
            font = config[role]
            base = FONTSOURCE_URL.format(
                name=font["name"], version=config["version"]
            )
            downloads[f"fonts/LICENSE-{font['name']}"] = f"{base}/LICENSE"
            families = set()
            for weight in font["weights"]:
                for style in ("", "-italic"):
                    source = self.fetch(f"{base}/{weight}{style}.css").decode()
                    for family, woff2, rule in self.font_faces(
                        source, font["name"], config["subsets"]
                    ):
                        families.add(family)
                        downloads[f"fonts/{woff2}"] = f"{base}/files/{woff2}"
                        css.append(f"\n{rule}\n")
            if len(families) != 1:
                raise ValueError(
                    f"Expected one font family for {font['name']}: {families}"
                )
            variables.append(f'  --md-{role}-font: "{families.pop()}";\n')
        css.append("\n:root {\n" + "".join(variables) + "}\n")
        return downloads, "".join(css)

    def prune(self, dest: Path, keep: set[str]) -> None:
        """Remove files and empty directories in dest not listed in keep."""
        for path in sorted(dest.rglob("*"), reverse=True):
            if path.is_dir():
                if not any(path.iterdir()):
                    path.rmdir()
            elif path.relative_to(dest).as_posix() not in keep:
                print(f"Removing {path}")
                path.unlink()


def main() -> None:
    VendorAssets()()


if __name__ == "__main__":
    main()
