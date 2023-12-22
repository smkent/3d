# Troubleshooting

## Print bed offset and leveling

Most common 3D printing issues are caused by the bed not being level or the
Z-offset being set incorrectly. Prints may warp or not stick to the build plate
at all if the print bed is not calibrated. The print bed calibration needs to be
redone periodically as printers wear in their parts.

### Z-offset

To check if the Z-offset is accurate, print a small single-layer (0.2mm) shape.
This can be done in PrusaSlicer without any model files:

![Creating a Z-offset test model in PrusaSlicer][prusaslicer-z-offset-test]{ .thumb }

Print the created model and compare it to these samples:

![Z-offset result samples][photo-z-offset-samples]{ .thumb }

Adjust the **Z offset** value as described in
[**First Print Guide's Printer first-time calibration**][printer-calibration-z-offset].

### Bed leveling

To check the overall bed leveling adjustment, print a similar model as the
Z-offset test but covering more of the print bed. Many models are available for
this purpose.

!!! note

    Many test models are sized for smaller printers than the SV06 Plus. You can
    increase a model's size in PrusaSlicer to match the size of the SV06 Plus
    print bed.

* [:simple-printables:{ .printables } SV06 Bed Level Test Print][weware-sv06-bed-level-test-print] by Weware
* [:simple-printables:{ .printables } 5 Minute Bed Leveling Test][tac0man-bed-level-test] by tac0man
* [:simple-thingiverse:{ .thingiverse } Ender3 Perfect Bed Leveling][thanapolboss-perfect-bed-leveling] by thanapolboss



If the first layer on a one of these printed models looks different on different
areas of the print bed, it's likely the bed leveling scan needs to be re-run.

Rerun **bed leveling** as described in
[**First Print Guide's Printer first-time calibration**][printer-calibration-leveling-the-bed].

## Further reading

For a more comprehensive guide, see these links:

* [Simplify3D's Print Quality troubleshooting Guide][simplify3d-print-quality-troubleshooting]
* [All3DP's 3D Printing Troubleshooting: All Problems & Solutions][all3dp-troubleshooting]


[all3dp-troubleshooting]: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
[photo-z-offset-samples]: ../img/photo-z-offset-samples.jpg
[printer-calibration-leveling-the-bed]: ../first-print/printer-calibration.md#leveling-the-bed
[printer-calibration-z-offset]: ../first-print/printer-calibration.md##setting-the-nozzle-height-offset-z-offset
[prusaslicer-z-offset-test]: ../img/prusaslicer-z-offset-test.webp
[simplify3d-print-quality-troubleshooting]: https://www.simplify3d.com/resources/print-quality-troubleshooting/
[tac0man-bed-level-test]: https://www.printables.com/model/200367-5-minute-bed-leveling-test
[thanapolboss-perfect-bed-leveling]: https://www.thingiverse.com/thing:4711071
[weware-sv06-bed-level-test-print]: https://www.printables.com/model/487645-sv06-bed-level-test-print
