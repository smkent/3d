# PrusaSlicer first-time configuration wizard

!!! tip

    Click any of the screenshots for a full-size or zoomable view.

When Starting PrusaSlicer for the first time, a configuration wizard appears:

![PrusaSlicer wizard welcome page][prusaslicer-wizard-1]{class="psimg" data-gallery="pswiz"}


Click **Next** at the bottom to proceed through the wizard.

## Printer selection

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

## Filament profiles

PrusaSlicer has both generic presets for various printing materials as well as
specific presets for specific filaments. I have had good success using the
generic profiles. [PLA][wiki-pla] and [PETG][wiki-petg] are common filaments, so
start with the generic filament profiles for each. Uncheck the other preselected
filaments in the Filament Profiles Selection
wizard page, and then click **Next**.

![PrusaSlicer wizard filament profiles selection page][prusaslicer-wizard-7]{class="psimg" data-gallery="pswiz"}

## Automatic updates

PrusaSlicer will check for application and configuration preset updates by
default. I recommend leaving these checked. Click **Next** to continue.

![PrusaSlicer wizard automatic updates page][prusaslicer-wizard-8]{class="psimg" data-gallery="pswiz"}

## Optional settings

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

## View mode

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


[printables]: https://printables.com
[prusaslicer-init-1]: ../img/prusaslicer-init-1.png
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
[wiki-petg]: https://en.wikipedia.org/wiki/PETG
[wiki-pla]: https://en.wikipedia.org/wiki/Polylactic_acid
