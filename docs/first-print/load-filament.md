# Loading filament

## Prepare filament

I recommend making your first print using [PLA][wiki-pla]. It's an easier
material to print with and a small spool of PLA filament is included with the
SV06 Plus.

Place the roll of filament you'd like to print with onto the printer's spool
holder. Make a clean cut near the end of the filament, at a ~45° angle.

![Cutting the filament at an angle][photo-cut-filament]{ .thumb }

## Position extruder

Turn on the printer.

Loading filament is best done some space between the nozzle and print bed. If
the extruder is all the way at the bottom, the extruder should be raised using
the LCD controls. On the movement menu on the LCD, tap the **+Z** button a few
times to raise the extruder.

![Raising the Z height on the LCD][lcd-raise-z]{ .off-glb }

Alternatively, a specific **Z** value can be entered manually. The extruder will
then move to the selected height.

![Setting Z to 50mm on the LCD][lcd-set-z-50]{ .off-glb }

## Filament loading methods

There are two ways turn the extruder to load filament.
[The extruder can be turned by hand](#loading-filament-manually)
after unlocking the motor, or
[turned a specific amount using the LCD menu](#loading-with-lcd-controls).

### Loading with LCD controls

#### Heat the nozzle

On the LCD's main menu, tap the gear icon in the bottom row, and then tap
**Refuel**.

![Refuel option selection on the LCD][lcd-refuel-select]{ .off-glb }

On this menu, you can tell the extruder to turn backwards or forwards to remove
or add filament.

Tap the **Feed** button. Since the nozzle heater is off, the printer will prompt
you to preheat the nozzle to **200°C**. Tap **Yes**, and wait for the nozzle to
heat up.

![Selecting filament feed and heat up prompt on the LCD][lcd-feed-heat]{ .off-glb }

#### Insert filament

Guide this end of the filament through the filament runout sensor, and then down
into the extruder's filament input on the top until you feel the filament stop
moving.

![Inserting filament into the extruder inlet][clip-insert-filament]{ .thumb }

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

Continue reading at [Remove excess](#remove-excess).

### Loading filament manually

#### Heat the nozzle

On the LCD's main menu, tap the nozzle temperature display to open the
temperature controls. Select the nozzle temperature and enter **210°C**. The
nozzle will begin to heat. Tap **&lt;** to return to the main menu.

#### Unlock extruder motor

The printer's stepper motors, including the extruder's motor, normally hold
their position so the printer's firmware stays in sync with its actual position
on each axis.

To load filament manually, the motors must be disengaged, or **unlocked**.

Tap the movement icon on the bottom left corner of the LCD. On this menu, tap
the extruder :material-lightning-bolt: icon to unlock the motors.

![Unlocking the motors on the LCD][lcd-unlock-motors]{ .off-glb }

#### Insert filament

Guide this end of the filament through the filament runout sensor, and then down
into the extruder's filament input on the top until you feel the filament stop
moving.

![Inserting filament into the extruder inlet][clip-insert-filament]{ .thumb }

#### Turn extruder wheel

Turn the extruder wheel clockwise with your finger. The extruder will begin to
draw in the filament.

![Turning the extruder wheel manually][clip-turn-extruder]{ .thumb }

After a few moments, filament should start coming out of the
heated nozzle on the bottom of the extruder.

![Photo of filament coming out of the nozzle][photo-filament-load-extrusion]{ .thumb }

## Remove excess

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


[clip-insert-filament]: ../img/clip-insert-filament.webp
[clip-remove-extra-filament]: ../img/clip-remove-extra-filament.webp
[clip-turn-extruder]: ../img/clip-turn-extruder.webp
[lcd-feed-distance]: ../img/lcd-feed-distance.webp
[lcd-feed-heat]: ../img/lcd-feed-heat.webp
[lcd-raise-z]: ../img/lcd-raise-z.webp
[lcd-refuel-back]: ../img/lcd-refuel-back.jpg
[lcd-refuel-hot-feed]: ../img/lcd-refuel-hot-feed.jpg
[lcd-refuel-select]: ../img/lcd-refuel-select.webp
[lcd-set-z-50]: ../img/lcd-set-z-50.webp
[lcd-unlock-motors]: ../img/lcd-unlock-motors.webp
[photo-cut-filament]: ../img/photo-cut-filament.jpg
[photo-filament-load-extrusion]: ../img/photo-filament-load-extrusion.jpg
[wiki-pla]: https://en.wikipedia.org/wiki/Polylactic_acid
