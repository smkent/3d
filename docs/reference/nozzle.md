# Nozzle replacement

3D printer nozzles wear out and occasionally need to be replaced. Nozzles can
also be changed to use a nozzle with a different diameter or made of a different
material.

Most 3D printers, including the Sovol SV06 Plus, come with a 0.4mm brass nozzle.
Nozzles made of hardened steel cost a bit more but last longer. Larger nozzles
allow faster printing at lower resolution (fewer layers).

## Replacement steps

Nozzles should be replaced while the heat block is at the machine's maximum
temperature. The nozzle will be hot when it is removed. Have a plate, silicone
mat, or similar surface ready where the removed hot nozzle can be placed.

* If the printer has not homed, home the printer using the **Home**
  (:material-home:) button in the movement controls on the LCD.

* As replacing the nozzle involves accessing the underside of the extruder, the
  extruder should be positioned high enough to access the nozzle. Use the
  movement controls on the LCD to raise the extruder to 200mm or higher.

* Remove the silicone sock from the heat block.

* If filament is loaded, heat the nozzle to the filament's printing temperature
  and remove the filament.

* Heat the nozzle to the **300°C** (the maximum temperature) using the LCD
  temperature controls.

* Using the nozzle wrench, gently unscrew the nozzle until it comes out of the
  heat block.

    !!! warning
        The nozzle is extremely hot! Be careful not to touch the nozzle in the
        wrench.

* Without touching the nozzle, dump the nozzle out of the wrench somewhere safe
  where it can cool. (The nozzle should be cool enough to touch within a few
  minutes.)

* Without touching the end of the nozzle wrench, place the new nozzle into the
  wrench with the screw threads facing upward.

    !!! warning
        The end of the nozzle wrench is still hot! Be careful not to touch it
        when inserting the new nozzle.

* Gently screw the nozzle into the heat block until it no longer turns. Ensure
  the nozzle is snugly inserted but do not overtighten it.

* Turn off the nozzle heater by setting the nozzle to **0°C** using the LCD
  temperature controls.

* After the nozzle and heat block have cooled enough to be safely touched,
  re-install the silicone sock. The bump-out part faces the rear of the
  extruder.

* Verify or re-calibrate the printer's **Z-offset** as described in
[**First Print Guide's Printer first-time calibration**][printer-calibration-z-offset].

## Additional resources

* [:fontawesome-brands-youtube:{ .youtube } How to replace the SV06 nozzle][hobby-hoarder-hotend-nozzle] by Sovol

    !!! note
        The SV06 and SV06 Plus use different types of nozzles. However,
        replacing the nozzle on any 3D printer is the same general process.

* [:fontawesome-brands-youtube:{ .youtube } Hotend explained and how to properly change the nozzle on a 3D printer][hobby-hoarder-hotend-nozzle] by Hobby Hoarder


[hobby-hoarder-hotend-nozzle]: https://www.youtube.com/watch?v=OzRAVkXjw3I
[printer-calibration-z-offset]: ../first-print/printer-calibration.md##setting-the-nozzle-height-offset-z-offset
[sovol-sv06-replace-nozzle]: https://www.youtube.com/watch?v=B0Kz2Hi6jxc
