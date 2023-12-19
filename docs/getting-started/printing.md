# Printing

It's time to make your first 3D print!

## Pick a model

First, decide what you'd like to print! Two popular models to start with are:

* [**Cali Cat - The Calibration Cat**][calicat] was my first print! The
  examples on this page will use Cali Cat.
* [**#3DBenchy**][benchy], or "Benchy," a little boat and a very popular
  calibration model.

Download the files for the model you choose.

![Thingiverse Cali Cat download button][thingiverse-calicat-download]{class="psimg" data-gallery="calicat"}

Your browser will download a ZIP file, which contains one or more model files
(generally in STL format). Unzip the ZIP file to a new folder on your
computer.

## Connect microSD card

The instructions for the printer to use will be saved on a microSD card. Connect
a microSD card to your computer so files can be saved on it.

## Slice model

A 3D model is a representation of a 3-dimensional object. A 3D model needs to be
"sliced," or converted, into a set of instructions for the printer to follow
called G-code.

Start PrusaSlicer. The default view is the Plater, or the build plate preview.

!!! info

    The **build plate** is the flexible steel sheet that sits on top of the heated
    print bed on the printer.

![PrusaSlicer main page showing the plater][prusaslicer-plater]{class="psimg" data-gallery="psprint"}

### Select print settings

The top three drop-downs in the right pane are the print presets. Each time you
prepare (slice) a model, check that the correct presets are selected. The three
types of presets are:

1. **Layer height**: How high each printed layer should be. Taller layers print
   faster (since fewer layers are needed), but the resulting object won't be as
   strong. The options in this drop-down also depend on the size of nozzle
   installed on your printer. Nearly all printers, including the Sovol SV06
   Plus, default to a 0.4mm nozzle. A good default layer height is half of the
   nozzle size, or in this case 0.2mm. The default selected print profile,
   **0.2mm SPEED**, is a good choice for most prints.

2. **Filament**: Filament is the material that printer uses to make an object.
   There are many types of filament. A very common and beginner-friendly type of
   filament is called polylactic acid, or **PLA**. On first run, PrusaSlicer
   defaults to PETG, a different type of material. Click the **Filament**
   drop-down and change the selection to **Generic PLA**.
   ![PrusaSlicer PLA material selection][prusaslicer-material-selection-pla]{class="psimg" data-gallery="psprint"}

3. **Printer**: The printer to make G-code for. PrusaSlicer will default to the
   custom **Sovol SV06 Plus** profile created after following the previous
   [Slicer setup][slicer-setup] guide.

### Load model

Loading the model you'd like to print into PrusaSlicer is called **importing**
the model.

!!! note

    Import and open in PrusaSlicer are different. Open takes a project file
    instead of a model file.

Import your chosen model file (such as Cali Cat's `calicat.stl`) by doing one of:

* Dragging and dropping `calicat.stl` from your file manager onto the open
  PrusaSlicer window
* Clicking the **Add** button on the top toolbar in the Plater view, and
  selecting `calicat.stl` in the file browser
  ![PrusaSlicer toolbar add button][prusaslicer-toolbar-add]{ .off-glb }
* Using the keyboard shortcut `Ctrl`+`I` (⌘`I` on Mac), and selecting `calicat.stl`
  in the file browser

Cali Cat will appear on the build plate in the Plater view.

![PrusaSlicer model import][prusaslicer-model-import]{class="psimg" data-gallery="psprint"}

### Slice!

For your first print, all of the remaining default settings can be kept.

On the bottom of the right pane, click **Slice now**!

![PrusaSlicer slicing model][prusaslicer-slice-now]{class="psimg" data-gallery="psprint"}

After slicing the model, PrusaSlicer displays two important estimates:

* The amount of filament predicted to be used in grams
* The length of time the print is expected to take

PrusaSlicer estimates Cali Cat will need around 7 grams of filament and will
take 50 minutes to print.

![PrusaSlicer estimates for Cali Cat][prusaslicer-estimates]{class="psimg" data-gallery="psprint"}

### Export G-code

Slicing has created G-code that the printer can use. With a microSD card
connected to your computer, there is a small icon on the very bottom right for
saving the G-code to the microSD card.

![PrusaSlicer microSD card export button][prusaslicer-microsd-card-button]{class="psimg" data-gallery="psprint"}

Alternatively, you can click the Export G-Code button (in the same place where
"Slice now" used to be) to save the file manually.

Export the generated G-code to the microSD card.

![PrusaSlicer export G-code to microSD card][prusaslicer-export-to-microsd-card]{class="psimg" data-gallery="psprint"}

## Safely remove microSD card

The microSD card is ready for the printer. Select the option to safely eject or
remove the microSD card in your computer's file manager. Then, disconnect it
from the computer.

## Load filament into the printer

Place the roll of filament you'd like to print with onto the printer's spool
holder. Make a clean snip at the end of the filament, at a ~45° angle.

Turn on the printer.

Loading filament is best done some space between the nozzle and print bed. If
the extruder is all the way at the bottom, the extruder should be raised using
the LCD controls. On the movement menu on the LCD, tap the **Z** value and enter
a value 30 to 50 millimeters greater than the displayed value (which is likely
0mm). The extruder will then move upwards to the selected position.

On the LCD's main menu, tap the gear icon in the bottom row, and then tap
**Refuel**. This menu allows you to turn the extruder backwards or forwards to
remove or add filament. I find **80mm** is a good distance value to use for
loading filament, but you can always extrude more (or less) if this value
doesn't fully load or unload filament.

Tap the **Feed** button. Since the nozzle heater is off, the printer will prompt
you to preheat the nozzle to **200°C**. Tap **Yes**, and wait for the nozzle to
heat up.

Guide this end of the filament through the filament runout sensor, and then down
into the extruder's filament input on the top until you feel the filament stop
moving.

Tap the **Feed** button again. The extruder motor will turn and start to draw
in the filament. After a few moments, filament should start coming out of the
heated nozzle on the bottom of the extruder. If the extruder stops turning
before filament comes out of the nozzle, then the extruder needs to turn
forwards more to push the filament through the nozzle. Tap **Feed** again to
repeat the process.

After filament comes out of the nozzle and the extruder stops turning, filament
is loaded and ready to print! Being *very careful* not to touch the hot nozzle,
you can reach in to remove the piece of dangling filament so it doesn't get in
the way when you print.

Tap the back button on the LCD to return to the main menu.


[benchy]: https://www.thingiverse.com/thing:763622
[calicat]: https://www.thingiverse.com/thing:1545913
[thingiverse-calicat-download]: ../img/thingiverse-calicat-download.png
[prusaslicer-plater]: ../img/prusaslicer-plater.png
[prusaslicer-estimates]: ../img/prusaslicer-estimates.png
[prusaslicer-toolbar-add]: ../img/prusaslicer-toolbar-add.png
[prusaslicer-model-import]: ../img/prusaslicer-model-import.gif
[prusaslicer-microsd-card-button]: ../img/prusaslicer-microsd-card-button.png
[prusaslicer-material-selection-pla]: ../img/prusaslicer-material-selection-pla.png
[prusaslicer-slice-now]: ../img/prusaslicer-slice-now.gif
[prusaslicer-export-to-microsd-card]: ../img/prusaslicer-export-to-microsd-card.gif
[slicer-setup]: ../slicer-setup/
