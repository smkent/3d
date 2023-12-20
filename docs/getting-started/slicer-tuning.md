# Tuning PrusaSlicer for the Sovol SV06 Plus

PrusaSlicer's default settings for the SV06 Plus are pretty good, but there are
a few tweaks I recommend making.

!!! tip

    My full PrusaSlicer configuration, including these customizations, is
    available on GitHub as
    [smkent/prusa-slicer-config][github-prusa-slicer-config].

## Retraction settings

The printer retracts (rewinds) filament when moving from one print line to
another. The default configuration causes the printer to retract filament even
when making very short moves, which isn't necessary and slows down printing when
creating filled-in surfaces. I recommend adjusting these settings.

Steps:

* Click the **Printer Settings** tab at the top
* In the left panel, select **Extruder 1**
* Scroll down to the **Retraction** section in the settings pane
* Change **Minimum travel after retraction** from 0.5 to **2**.
* Uncheck (disable) **Wipe while retracting**.

Steps animation:

![PrusaSlicer retraction settings adjustment][prusaslicer-retraction-settings]{class="psimg" data-gallery="psprintprofile"}

## G-code flavor

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

## Custom print bed display

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

## Saving printer settings

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
[github-prusa-slicer-config]: https://github.com/smkent/prusa-slicer-config
[marlin]: https://marlinfw.org/
[prusaslicer-bed-texture]: ../img/prusaslicer-bed-texture.gif
[prusaslicer-data-collection]: ../img/prusaslicer-data-collection.png
[prusaslicer-g-code-flavor]: ../img/prusaslicer-g-code-flavor.gif
[prusaslicer-github-releases]: https://github.com/prusa3d/PrusaSlicer/releases
[prusaslicer-retraction-settings]: ../img/prusaslicer-retraction-settings.gif
[prusaslicer-save-printer-preset]: ../img/prusaslicer-save-printer-preset.gif
[sovol-sv06-plus-complete-assembly]: https://github.com/Sovol3d/SV06-PLUS/blob/master/SV06%20PLUS%203D/STEP/SV06%20Plus%20Complete%20Assembly%20300x300x340.rar
