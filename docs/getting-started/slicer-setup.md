# Slicer setup

A 3D printer works by building an object layer by layer. To print an object from
a 3D model, a set of instructions on how to create the model layer-by-layer
needs to be created. These instructions are called **G-code**. G-code is created
using a type of software called a **slicer**.

There are many slicer softwares available. Two popular options are
[PrusaSlicer][prusaslicer] and [Ultimaker Cura][cura], which are free and open
source.

For the Sovol SV06 Plus, I've had the best results using PrusaSlicer.

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

## Configuration wizard

!!! tip

    Click any of the screenshots for a full-size or zoomable view.

When Starting PrusaSlicer for the first time, a configuration wizard appears:

![PrusaSlicer wizard welcome page][prusaslicer-wizard-1]{class="psimg" data-gallery="pswiz"}


Click **Next** at the bottom to proceed through the wizard.

### Printer selection

The first several pages in the configuration wizard lead you through the
supported printers. By default, a Prusa printer preset is selected. Uncheck the
checkbox under Original Prusa MK4 Input Shaper, and click **Next** to continue.

![PrusaSlicer wizard Prusa FFF printers page][prusaslicer-wizard-2]{class="psimg" data-gallery="pswiz"}

The next page provides options for Prusa SLA (resin) printers. Leave these
unchecked and click **Next**.

![PrusaSlicer wizard Prusa SLA printers page][prusaslicer-wizard-3]{class="psimg" data-gallery="pswiz"}

Then, the configuration wizard provides options for selecting printers from
other brands. The SV06 Plus is made by Sovol, so scroll down in the vendors list
and click the **Sovol** checkbox. Then, click **Next**.

![PrusaSlicer wizard printer vendors selection page][prusaslicer-wizard-4]{class="psimg" data-gallery="pswiz"}

Now the configuration wizard provides options for selecting Sovol printers. By
default, a SV06 preset is selected. Uncheck the **SV06** checkbox, and
then check the **SV06 Plus 0.4mm nozzle** checkbox. Then, click **Next**.

![PrusaSlicer wizard Sovol printer presets page][prusaslicer-wizard-5]{class="psimg" data-gallery="pswiz"}

The last printer selection page in the configuration wizard offers to provide a
custom printer profile. Since there is a built-in preset for the SV06 Plus, a
custom profile is not needed. Click **Next**.

![PrusaSlicer wizard custom printer profile page][prusaslicer-wizard-6]{class="psimg" data-gallery="pswiz"}

### Filament profiles

PrusaSlicer has both generic presets for various printing materials as well as
specific presets for specific filaments. I have had good success using the
generic profiles. This guide will focus in printing with [PLA][wiki-pla] and
[PETG][wiki-petg] filaments starting with the generic filament profiles for
each. Uncheck the other preselected filaments in the Filament Profiles Selection
wizard page, and then click **Next**.

![PrusaSlicer wizard filament profiles selection page][prusaslicer-wizard-7]{class="psimg" data-gallery="pswiz"}

### Automatic updates

PrusaSlicer will check for application and configuration preset updates by
default. I recommend leaving these checked. Click **Next** to continue.

![PrusaSlicer wizard automatic updates page][prusaslicer-wizard-8]{class="psimg" data-gallery="pswiz"}

### Optional settings

On this page, you can optionally enable PrusaSlicer's browser integration. With
this enabled, you can click the PrusaSlicer logo next to a model file on
[Printables][printables] and have it automatically download and open in
PrusaSlicer. When finished configuring this feature, click **Next**.

![PrusaSlicer wizard download from URL settings page][prusaslicer-wizard-9]{class="psimg" data-gallery="pswiz"}

The reload from disk feature makes reloading model files easier while you're
developing a new model. Enabling this feature includes full file paths in your
saved project files (which would include your username on your local computer).
If you plan to share project files on the internet, it's a good idea to leave
this disabled (unchecked). After making your choice, click **Next**.

![PrusaSlicer wizard reload from disk settings page][prusaslicer-wizard-10]{class="psimg" data-gallery="pswiz"}

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

![PrusaSlicer wizard view mode page][prusaslicer-wizard-11]{class="psimg" data-gallery="pswiz"}

PrusaSlicer now shows the main view. This is where PrusaSlicer will open each
time it is run.

![PrusaSlicer initial view][prusaslicer-init-1]{class="psimg" data-gallery="psinit"}

## Tuning configuration

PrusaSlicer's default settings for the SV06 Plus are pretty good, but there are
a few tweaks I recommend making.

!!! tip

    My full PrusaSlicer configuration, including these customizations, is
    available on GitHub as
    [smkent/prusa-slicer-config][github-prusa-slicer-config].

### Retraction settings

The printer retracts (rewinds) filament when moving from one print line to
another. The default configuration retracts for very small moves, which slows
down printing when creating filled-in surfaces. I recommend adjusting these
settings.

Steps:

* Click the **Printer Settings** tab at the top
* In the left panel, select **Extruder 1**
* Scroll down to the **Retraction** section in the settings pane
* Change **Minimum travel after retraction** from 0.5 to **2**.
* Uncheck (disable) **Wipe while retracting**.

Steps animation:

![PrusaSlicer retraction settings adjustment][prusaslicer-retraction-settings]{class="psimg" data-gallery="psprintprofile"}

### G-code flavor

Each printer has its own internal firmware which interprets the G-code created
by a slicer. The G-code types can vary from one printer to another. The SV06
Plus uses a firmware called [Marlin][marlin].

PrusaSlicer configures the SV06 Plus to create older-style Marlin G-code by
default. The SV06 Plus ships with Marlin version 2.0.9.2 and can support a
newer G-code profile in PrusaSlicer. I recommend changing the G-code flavor
from "Marlin (legacy)" to "Marlin 2."

Steps:

* Click the **Printer Settings** tab at the top
* In the left panel, select **General** (the first item)
* In the **Firmware** section, change **G-code flavor** from Marlin (legacy) to
  **Marlin 2**

Steps animation:

![PrusaSlicer G-code flavor adjustment][prusaslicer-g-code-flavor]{class="psimg" data-gallery="psprintprofile"}

### Custom print bed display

This tweak is purely a visual preference within PrusaSlicer. I like to use a
more accurate print bed model image in the model preview.

First, save these two files to a folder on your computer:

* [`sovol-sv06-plus-texture-white-logo.png`](../static/sovol-sv06-plus-texture-white-logo.png).
  This is a print bed image I like, from [Catfisher4's SV06 Plus Build Plate Package][catfisher4-build-plate-package].
* [`sovol-sv06-plus-model.stl`](../static/sovol-sv06-plus-model.stl). This is
  a print bed mesh model, which I exported from Sovol's
  [complete assembly model][sovol-sv06-plus-complete-assembly].

Then, follow these steps to update the print bed configuration in PrusaSlicer:

* Click the **Printer Settings** tab at the top
* In the left panel, select **General** (the first item)
* In the **Size and Coordinates** section at the top, click the **Bed shape**
  option's **Set** button. A dialog will appear.
* In the dialog's **Texture** section, click **Load**. Find the folder where you
  saved `sovol-sv06-plus-texture-white-logo.png` and select that file.
* In the dialog's **Model** section, click **Load**. Find the folder where you
  saved `sovol-sv06-plus-model.stl` and select that file.
* Click **OK** to close the dialog
* Click the **Plater** tab at the top to return to the main view. The updated
  print bed texture is now visible.

Steps animation:

![PrusaSlicer bed texture configuration][prusaslicer-bed-texture]{class="psimg" data-gallery="psprintprofile"}

### Saving printer settings

Now all that's left is to save these changes to a new printer preset.

PrusaSlicer tracks configuration via presets, which work in a hierarchical
fashion. By creating a new printer preset, PrusaSlicer will use all of the
default settings from the SV06 Plus preset plus the settings changes made
above.

Steps:

* Click the **Printer Settings** tab at the top
* The printer presets drop-down is at the top, with "SV06 PLUS (modified)" selected.
  Click the save icon just to the right of that drop-down. A dialog will appear.
* Enter a name for your new printer preset, such as **Sovol SV06 Plus**
* Click **OK** to save this new printer preset
* The new preset is now the active printer preset, seen in both the Printer
  Settings tab and again on the Plater tab (main view).

Steps animation:

![PrusaSlicer saving new printer preset][prusaslicer-save-printer-preset]{class="psimg" data-gallery="psprintprofile"}


[catfisher4-build-plate-package]: https://www.printables.com/model/534551-sovol-sv06-plus-build-plate-package-texture-and-mo
[cura]: https://ultimaker.com/software/ultimaker-cura/
[github-prusa-slicer-config]: https://github.com/smkent/prusa-slicer-config
[marlin]: https://marlinfw.org/
[printables]: https://printables.com
[prusaslicer-bed-texture]: ../img/prusaslicer-bed-texture.gif
[prusaslicer-data-collection]: ../img/prusaslicer-data-collection.png
[prusaslicer-g-code-flavor]: ../img/prusaslicer-g-code-flavor.gif
[prusaslicer-github-releases]: https://github.com/prusa3d/PrusaSlicer/releases
[prusaslicer-init-1]: ../img/prusaslicer-init-1.png
[prusaslicer-retraction-settings]: ../img/prusaslicer-retraction-settings.gif
[prusaslicer-save-printer-preset]: ../img/prusaslicer-save-printer-preset.gif
[prusaslicer-ssl-certs]: ../img/prusaslicer-ssl-certs.png
[prusaslicer-wizard-10]: ../img/prusaslicer-wizard-10.png
[prusaslicer-wizard-11]: ../img/prusaslicer-wizard-11.png
[prusaslicer-wizard-1]: ../img/prusaslicer-wizard-1.png
[prusaslicer-wizard-2]: ../img/prusaslicer-wizard-2.png
[prusaslicer-wizard-3]: ../img/prusaslicer-wizard-3.png
[prusaslicer-wizard-4]: ../img/prusaslicer-wizard-4.png
[prusaslicer-wizard-5]: ../img/prusaslicer-wizard-5.png
[prusaslicer-wizard-6]: ../img/prusaslicer-wizard-6.png
[prusaslicer-wizard-7]: ../img/prusaslicer-wizard-7.png
[prusaslicer-wizard-8]: ../img/prusaslicer-wizard-8.png
[prusaslicer-wizard-9]: ../img/prusaslicer-wizard-9.png
[prusaslicer]: https://www.prusa3d.com/page/prusaslicer_424/
[sovol-sv06-plus-complete-assembly]: https://github.com/Sovol3d/SV06-PLUS/blob/master/SV06%20PLUS%203D/STEP/SV06%20Plus%20Complete%20Assembly%20300x300x340.rar
[wiki-petg]: https://en.wikipedia.org/wiki/PETG
[wiki-pla]: https://en.wikipedia.org/wiki/Polylactic_acid
