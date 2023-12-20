# Printing

Now you're ready to learn how to print a model with the printer!

## Pick a model

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

As explained before on [Slicer setup][slicer-setup], a 3D model is a
representation of a 3-dimensional object. A 3D model needs to be "sliced," or
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

## Load filament

Place the roll of filament you'd like to print with onto the printer's spool
holder. Make a clean snip at the end of the filament, at a ~45° angle.

Turn on the printer.

Loading filament is best done some space between the nozzle and print bed. If
the extruder is all the way at the bottom, the extruder should be raised using
the LCD controls. On the movement menu on the LCD, tap the **+Z** a few times to
raise the extruder.

![Raising the Z height on the LCD][lcd-raise-z]{ .off-glb }

Alternatively, a specific **Z** value can be entered manually. The extruder will
then move to the selected height.

![Setting Z to 50mm on the LCD][lcd-set-z-50]{ .off-glb }

On the LCD's main menu, tap the gear icon in the bottom row, and then tap
**Refuel**.

![Refuel option selection on the LCD][lcd-refuel-select]{ .off-glb }

This menu allows you to turn the extruder backwards or forwards to
remove or add filament.

Tap the **Feed** button. Since the nozzle heater is off, the printer will prompt
you to preheat the nozzle to **200°C**. Tap **Yes**, and wait for the nozzle to
heat up.

![Selecting filament feed and heat up prompt on the LCD][lcd-feed-heat]{ .off-glb }

Guide this end of the filament through the filament runout sensor, and then down
into the extruder's filament input on the top until you feel the filament stop
moving.

I find **80mm** is a good distance value to use for loading filament, but you
can always extrude more (or less) if this value doesn't fully load or unload
filament. The default distance value is 10mm which is very short. Enter a longer
distance value.

![Filament load distance value entry on the LCD][lcd-feed-distance]{ .off-glb }

Tap the **Feed** button again. The extruder motor will turn and start to draw
in the filament.

![Feed button on the refuel menu on the LCD][lcd-refuel-hot-feed]{ .off-glb }

After a few moments, filament should start coming out of the
heated nozzle on the bottom of the extruder.

![Photo of filament coming out of the nozzle][photo-filament-load-extrusion]{ .thumb }

If the extruder stops turning before filament comes out of the nozzle, then the
extruder needs to turn forwards more to push the filament through the nozzle. In
this case, tap **Feed** again to repeat the process.

After filament comes out of the nozzle and the extruder stops turning, filament
is loaded and ready to print! Being *very careful* not to touch the hot nozzle,
you can reach in to remove the piece of dangling filament so it doesn't get in
the way when you print.

![Removing extra filament from underneath the nozzle][clip-remove-extra-filament]{ .thumb }

Tap the **&lt;** button on the LCD to return to the main menu.

![Refuel menu back button on the LCD][lcd-refuel-back]{ .off-glb }

!!! warning

    If you decide not to print after loading filament, be sure to turn off the
    nozzle heater from the main menu using the temperature controls.

## Start the print

Now all that's left is to select the G-code file and start the print!

On the LCD's main menu, tap the large **+ Select the file** button, tap the
**calicat...** G-code file, and then tap **Print**.

![Selecting a file and starting a print on the LCD][lcd-select-start-print]{ .off-glb }

The printer will heat up the nozzle and heated bed to **210°C** and the heated
bed to **60°C**. These are the temperatures configured in PrusaSlicer for PLA.

!!! info

    If the printer displays different temperatures, that usually means the wrong
    filament / material preset was selected in your slicer (PrusaSlicer).

    In this case, tap the **Stop** button to stop the print, re-slice the model
    file in PrusaSlicer, save the new G-code file to the microSD card, and try
    your print again.

Once the nozzle and heated bed reach their configured temperatures, the LCD will
show an animation and the printer will start working!

![LCD print progress view][lcd-print-progress]{ .off-glb }

The printer will do several things each time it starts a print:

* The extruder will home (move to the furthest left, back, and down position) to
  re-establish its coordinate system
* The printer will draw a line of filament, either on the left or front side of
  the print bed, called a **purge line**. It is normal for some filament to ooze
  out of the nozzle before it starts moving. Creating a purge line before
  working on a model helps the printer to wipe off this extra filament so it
  doesn't get attached to the model.
* For most models, the printer will draw a border around the area where it will
  start printing the model. This is called a **skirt**. The skirt is a good
  visual indicator of the size of the model to be printed.
  [The skirt is configurable within PrusaSlicer][prusaslicer-skirt]
  when preparing a model.

!!! info

    If the skirt is a different size than you expected, it might mean you have
    selected a different file than you meant or that the print file isn't
    working properly.

    In this case, tap the **Stop** button to stop the print, re-slice the model
    file in PrusaSlicer, save the new G-code file to the microSD card, and try
    your print again.

* Finally, the printer will start building your model!

## Monitor the printer

With any luck, you'll start to recognize Cali Cat while it's being printed!

![Printing Cali Cat!][clip-printing-calicat]{ .thumb }

Sometimes, a print doesn't go as expected so it's a good idea to keep an eye on
the printer while it works. For example, the model being printed can come loose
from the build plate or the printer doesn't build the model as you expected. If
you don't stop the printer when this happens, you might be visited by the
**spaghetti monster**!

![Spaghetti monster][reddit-aargvark-spaghetti-monster]{ .thumb } <br />
<small>(Picture from [/u/aargvark on Reddit][reddit-aargvark-post])</small>

!!! info

    You can stop a print in progress using the **Stop** button on the LCD.

    If the printer needs to be stopped quickly, turn off the power switch.

After patiently waiting for about an hour, the printer will finish printing Cali
Cat!

Tap **Finish print** on the LCD to return to the main menu.

![Finished print information on the LCD][lcd-print-finished]{ .off-glb }

## Remove the finished print

When the printer finishes, I recommend waiting for the print bed to cool down 10
to 20 degrees Celsius. This helps prevent the finished print from deforming from
the bed heat when it is removed from the build plate.

The purge line can be removed with the printer's included scraper.

![Removing the purge line from the build plate with the scraper][clip-removing-purge-line]{ .thumb }

To remove a finished print from the build plate, grip the build plate handles
with your fingers and gently lift. Often times, a finished print will simply pop
off the build plate.

![Removing Cali Cat from the build plate][clip-removing-calicat]{ .thumb }

If a model has a larger surface area on the print bed (such as something low and
flat), you can lift the build plate off of the print bed and gently bend the
build plate inward, curving the surface off of the finished print.

After you've removed your finished print, place the build plate back on the
print bed with the notches aligned with the screws on the back end.

Remove any remaining filament from the print bed (e.g. the skirt).

![Removing the skirt from the build plate with the scraper][clip-removing-skirt]{ .thumb }

**Congratulations on your first 3D print!**

![Finished Cali Cat][photo-calicat-finished]{ .thumb }


[benchy]: https://www.thingiverse.com/thing:763622
[calicat]: https://www.thingiverse.com/thing:1545913
[clip-printing-calicat]: ../img/clip-printing-calicat.webp
[clip-remove-extra-filament]: ../img/clip-remove-extra-filament.webp
[clip-removing-calicat]: ../img/clip-removing-calicat.webp
[clip-removing-purge-line]: ../img/clip-removing-purge-line.webp
[clip-removing-skirt]: ../img/clip-removing-skirt.webp
[lcd-feed-distance]: ../img/lcd-feed-distance.webp
[lcd-feed-heat]: ../img/lcd-feed-heat.webp
[lcd-print-finished]: ../img/lcd-print-finished.jpg
[lcd-print-progress]: ../img/lcd-print-progress.webp
[lcd-raise-z]: ../img/lcd-raise-z.webp
[lcd-refuel-back]: ../img/lcd-refuel-back.jpg
[lcd-refuel-hot-feed]: ../img/lcd-refuel-hot-feed.jpg
[lcd-refuel-select]: ../img/lcd-refuel-select.webp
[lcd-select-start-print]: ../img/lcd-select-start-print.webp
[lcd-set-z-50]: ../img/lcd-set-z-50.webp
[photo-calicat-finished]: ../img/photo-calicat-finished.jpg
[photo-filament-load-extrusion]: ../img/photo-filament-load-extrusion.jpg
[prusaslicer-estimates]: ../img/prusaslicer-estimates.png
[prusaslicer-export-to-microsd-card]: ../img/prusaslicer-export-to-microsd-card.gif
[prusaslicer-material-selection-pla]: ../img/prusaslicer-material-selection-pla.png
[prusaslicer-microsd-card-button]: ../img/prusaslicer-microsd-card-button.png
[prusaslicer-model-import]: ../img/prusaslicer-model-import.gif
[prusaslicer-plater]: ../img/prusaslicer-plater.png
[prusaslicer-skirt]: https://help.prusa3d.com/article/skirt-and-brim_133969
[prusaslicer-slice-now]: ../img/prusaslicer-slice-now.gif
[prusaslicer-toolbar-add]: ../img/prusaslicer-toolbar-add.png
[reddit-aargvark-post]: https://old.reddit.com/r/Sovol/comments/13658vh/comment/jin66ha/
[reddit-aargvark-spaghetti-monster]: ../img/reddit-aargvark-spaghetti-monster.jpg
[slicer-setup]: slicer-setup.md
[thingiverse-calicat-download]: ../img/thingiverse-calicat-download.png
[wiki-g-code]: https://en.wikipedia.org/wiki/G-code
