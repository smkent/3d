# PrusaSlicer installation

## What is a slicer?

A 3D printer works by building an object layer by layer. To print an object from
a 3D model, a set of instructions on how to create the model layer-by-layer
needs to be created. These instructions are called **[G-code][wiki-g-code]**.
G-code is created using a type of software called a **[slicer][wiki-slicer]**.

There are many slicer softwares available. Two popular options are
[PrusaSlicer][prusaslicer] and [Ultimaker Cura][cura], which are free and open
source.

For the Sovol SV06 Plus, I've had the best results using **PrusaSlicer**.

## Installation

Download and install [PrusaSlicer][prusaslicer] on your computer. PrusaSlicer is
available for Windows, Mac OS X, and Linux. PrusaSlicer can alternatively be
downloaded from the
[PrusaSlicer repository on GitHub][prusaslicer-github-releases] (be sure to
select the right file for your operating system).

Start PrusaSlicer after it is installed. On first run, PrusaSlicer may show a
prompt about SSL certificates. Check **Remember my choice** and then click
**Yes**.

![SSL certificates dialog][prusaslicer-ssl-certs]{ .psimg .off-glb }

PrusaSlicer may also ask whether it's OK to send system information. This is
optional, so select whichever option you prefer.

![PrusaSlicer data collection prompt][prusaslicer-data-collection]{class="psimg" data-gallery="psdc"}

[cura]: https://ultimaker.com/software/ultimaker-cura/
[prusaslicer-data-collection]: ../img/prusaslicer-data-collection.png
[prusaslicer-github-releases]: https://github.com/prusa3d/PrusaSlicer/releases
[prusaslicer-ssl-certs]: ../img/prusaslicer-ssl-certs.png
[prusaslicer]: https://www.prusa3d.com/page/prusaslicer_424/
[wiki-g-code]: https://en.wikipedia.org/wiki/G-code
[wiki-slicer]: https://en.wikipedia.org/wiki/Slicer_(3D_printing)
