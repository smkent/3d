# Prepare a model to print

## Choose a model

First, decide what you'd like to print! Two popular models to start with are:

* [**Cali Cat - The Calibration Cat**][calicat] was my first print! The
  examples on this page will use Cali Cat.
* [**#3DBenchy**][benchy], or "Benchy," a little boat and a very popular
  calibration and benchmarking model.

Download the files for the model you choose.

![Thingiverse Cali Cat download button][thingiverse-calicat-download]{class="psimg" data-gallery="calicat"}

Your browser will download a ZIP file, which contains one or more model files
(generally in STL format). Unzip the ZIP file to a new folder on your
computer.

## Connect microSD card

The instructions for the printer to use will be saved on a microSD card. Connect
a microSD card to your computer so files can be saved on it.

## Slice model

As explained before on [Slicer installation][slicer-installation], a 3D model is
a representation of a 3-dimensional object. A 3D model needs to be "sliced," or
converted, into a set of instructions for the printer to follow called
[G-code][wiki-g-code].

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
   <br /><br />
   ![PrusaSlicer PLA material selection][prusaslicer-material-selection-pla]{class="psimg" data-gallery="psprint"}

3. **Printer**: The printer to make G-code for. PrusaSlicer will default to the
   custom **Sovol SV06 Plus** profile created after following the previous
   [Slicer tuning][slicer-tuning] guide.

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
  <br /><br />
  ![PrusaSlicer toolbar add button][prusaslicer-toolbar-add]{ .off-glb }
* Using the keyboard shortcut ++ctrl+i++ (++cmd+i++ on Mac), and selecting `calicat.stl`
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

## Move microSD card to printer

The microSD card is ready for the printer. Select the option to safely eject or
remove the microSD card in your computer's file manager.

Disconnect the microSD card from the computer, and insert it into the microSD
("TF") slot on the printer next to the Micro USB port. The top of the microSD
card should face inward (toward the print bed).


[benchy]: https://www.thingiverse.com/thing:763622
[calicat]: https://www.thingiverse.com/thing:1545913
[prusaslicer-estimates]: ../img/prusaslicer-estimates.png
[prusaslicer-export-to-microsd-card]: ../img/prusaslicer-export-to-microsd-card.gif
[prusaslicer-material-selection-pla]: ../img/prusaslicer-material-selection-pla.png
[prusaslicer-microsd-card-button]: ../img/prusaslicer-microsd-card-button.png
[prusaslicer-model-import]: ../img/prusaslicer-model-import.gif
[prusaslicer-plater]: ../img/prusaslicer-plater.png
[prusaslicer-skirt]: https://help.prusa3d.com/article/skirt-and-brim_133969
[prusaslicer-slice-now]: ../img/prusaslicer-slice-now.gif
[prusaslicer-toolbar-add]: ../img/prusaslicer-toolbar-add.png
[slicer-installation]: slicer-installation.md
[slicer-tuning]: slicer-tuning.md
[thingiverse-calicat-download]: ../img/thingiverse-calicat-download.png
[wiki-g-code]: https://en.wikipedia.org/wiki/G-code
