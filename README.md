# 3D printing with the Sovol SV06 Plus

[![Build](https://img.shields.io/github/checks-status/smkent/3d/main?label=build)][gh-actions]
[![GitHub stars](https://img.shields.io/github/stars/smkent/3d?style=social)][repo]

[![Site logo][logo]][site]

**View the site here: [3d.smkent.net][site]**

## Development

### [Poetry][poetry] installation

Via [`pipx`][pipx]:

```console
pip install pipx
pipx install poetry
pipx inject poetry poetry-pre-commit-plugin
```

Via `pip`:

```console
pip install poetry
poetry self add poetry-pre-commit-plugin
```

### Development tasks

#### Project setup

* Setup: `poetry install`
* Run static checks: `poetry run poe lint` or
  `poetry run pre-commit run --all-files`

#### Site development

* Start the live-reloading docs server: `poetry run mkdocs serve`
* Build the documentation site: `poetry run mkdocs build`

---

Created from [smkent/cookie-python][cookie-python] using
[cookiecutter][cookiecutter]

[cookie-python]: https://github.com/smkent/cookie-python
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[gh-actions]: https://github.com/smkent/3d/actions?query=branch%3Amain
[logo]: docs/img/logo-readme.png
[mkdocs]: https://www.mkdocs.org
[pipx]: https://pypa.github.io/pipx/
[poetry]: https://python-poetry.org/docs/#installation
[repo]: https://github.com/smkent/3d
[site]: https://3d.smkent.net
