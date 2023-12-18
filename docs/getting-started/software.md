# Software

A 3D printer works by building an object layer by layer. To print an object from
a 3D model, the model needs to be converted to a layer-by-layer representation
for the printer to use called **G-code**. This is done using a type of software
called a **slicer**.

There are many slicer softwares available. Two popular options are
[PrusaSlicer][prusaslicer] and [Ultimaker Cura][cura], which are free and open
source.

For the Sovol SV06 Plus, I've had the best results using PrusaSlicer.

## Installation

Download and install [PrusaSlicer][prusaslicer] on your computer. PrusaSlicer is
available for Windows, Mac OS X, and Linux.

Open PrusaSlicer after it is installed. On first run, PrusaSlicer may show a
prompt about SSL certificates. Check **Remember my choice** and then click
**Yes**.

![SSL certificates dialog][prusaslicer-ssl-certs]{ .off-glb }

## Configuration wizard

!!! tip

    Click any of the screenshots for a full-size or zoomable view.

When Starting PrusaSlicer for the first time, a configuration wizard appears:

![PrusaSlicer wizard welcome page][prusaslicer-wizard-1]{: data-gallery="pswiz"}


Click **Next** at the bottom to proceed through the wizard.

### Printer selection

The first several pages in the configuration wizard lead you through the
supported printers. By default, a Prusa printer profile is selected. Uncheck the
checkbox under Original Prusa MK4 Input Shaper, and click **Next** to continue.

![PrusaSlicer wizard Prusa FFF printers page][prusaslicer-wizard-2]{: data-gallery="pswiz"}

The next page provides options for Prusa SLA (resin) printers. Leave these
unchecked and click **Next**.

![PrusaSlicer wizard Prusa SLA printers page][prusaslicer-wizard-3]{: data-gallery="pswiz"}

Then, the configuration wizard provides options for selecting printers from
other brands. The SV06 Plus is made by Sovol, so scroll down in the vendors list
and click the **Sovol** checkbox. Then, click **Next**.

![PrusaSlicer wizard printer vendors selection page][prusaslicer-wizard-4]{: data-gallery="pswiz"}

Now the configuration wizard provides options for selecting Sovol printers. By
default, a SV06 profile is selected. Uncheck the **SV06** checkbox, and
then check the **SV06 Plus 0.4mm nozzle** checkbox. Then, click **Next**.

![PrusaSlicer wizard Sovol printer profiles page][prusaslicer-wizard-5]{: data-gallery="pswiz"}

The last printer selection page in the configuration wizard offers to provide a
custom printer profile. Since there is a built-in profile for the SV06 Plus, a
custom profile is not needed. Click **Next**.

![PrusaSlicer wizard custom printer profile page][prusaslicer-wizard-6]{: data-gallery="pswiz"}

### Filament profiles

PrusaSlicer has both generic presets for various printing materials as well as
specific presets for specific filaments. I have had good success using the
generic profiles. This guide will focus in printing with [PLA][wiki-pla] and
[PETG][wiki-petg] filaments starting with the generic filament profiles for
each. Uncheck the other preselected filaments in the Filament Profiles Selection
wizard page, and then click **Next**.

![PrusaSlicer wizard filament profiles selection page][prusaslicer-wizard-8]{: data-gallery="pswiz"}

### Optional settings

On this page, you can optionally enable PrusaSlicer's browser integration. With
this enabled, you can click the PrusaSlicer logo next to a model file on
[Printables][printables] and have it automatically download and open in
PrusaSlicer. When finished configuring this feature, click **Next**.

![PrusaSlicer wizard download from URL settings page][prusaslicer-wizard-9]{: data-gallery="pswiz"}

The reload from disk feature makes reloading model files easier while you're
developing a new model. Enabling this feature includes full file paths in your
saved project files (which would include your username on your local computer).
If you plan to share project files on the internet, it's a good idea to leave
this disabled (unchecked). After making your choice, click **Next**.

![PrusaSlicer wizard reload from disk settings page][prusaslicer-wizard-10]{: data-gallery="pswiz"}

### View mode

The view mode page is the last configuration wizard page. I recommend setting
the view mode to **Expert**, so all of the options will be visible when
preparing a model to print. Simple, advanced, and expert options will have a
green, yellow, or red dot next to them when preparing a model in PrusaSlicer.

Finally, I strongly recommend leaving "Use inches" **unchecked**, so that
PrusaSlicer will use millimeters. Nearly all model files on the internet use
millimeters for sizing, so using millimeters in PrusaSlicer makes working with
3D models easier.

Click **Finish** at the bottom to complete the wizard!

![PrusaSlicer wizard view mode page][prusaslicer-wizard-11]{: data-gallery="pswiz"}


[cura]: https://ultimaker.com/software/ultimaker-cura/
[prusaslicer-ssl-certs]: ../img/prusaslicer-ssl-certs.png
[prusaslicer]: https://www.prusa3d.com/page/prusaslicer_424/
[prusaslicer-wizard-1]: ../img/prusaslicer-wizard-1.png
[prusaslicer-wizard-2]: ../img/prusaslicer-wizard-2.png
[prusaslicer-wizard-3]: ../img/prusaslicer-wizard-3.png
[prusaslicer-wizard-4]: ../img/prusaslicer-wizard-4.png
[prusaslicer-wizard-5]: ../img/prusaslicer-wizard-5.png
[prusaslicer-wizard-6]: ../img/prusaslicer-wizard-6.png
[prusaslicer-wizard-7]: ../img/prusaslicer-wizard-7.png
[prusaslicer-wizard-8]: ../img/prusaslicer-wizard-8.png
[prusaslicer-wizard-9]: ../img/prusaslicer-wizard-9.png
[prusaslicer-wizard-10]: ../img/prusaslicer-wizard-10.png
[prusaslicer-wizard-11]: ../img/prusaslicer-wizard-11.png
[wiki-pla]: https://en.wikipedia.org/wiki/Polylactic_acid
[wiki-petg]: https://en.wikipedia.org/wiki/PETG
