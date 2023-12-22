# Troubleshooting

## Bed Level

Most common 3D printing issues are caused by the bed not being level or the
Z-offset being set incorrectly. Prints may warp or not stick to the build plate
at all if the print bed is not calibrated. The print bed calibration needs to be
redone periodically as printers wear in their parts.

To check if the Z-offset is accurate, print a small single-layer (0.2mm) shape.
This can be done in PrusaSlicer without any model files:

![Creating a Z-offset test model in PrusaSlicer][prusaslicer-z-offset-test]{ .thumb }

Print the created model and compare it to these samples:

![Z-offset result samples][photo-z-offset-samples]{ .thumb }

Adjust the **Z offset** value and rerun **bed leveling** by repeating the
corresponding steps in
[**First Print Guide's Printer first-time calibration**][printer-calibration].

## Further Reading

For a more comprehensive guide, see these links:

* [Simplify3D's Print Quality troubleshooting Guide][simplify3d-print-quality-troubleshooting]
* [All3DP's 3D Printing Troubleshooting: All Problems & Solutions][all3dp-troubleshooting]


[all3dp-troubleshooting]: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
[photo-z-offset-samples]: ../img/photo-z-offset-samples.jpg
[printer-calibration]: ../first-print/printer-calibration.md#preparation-for-bed-calibration
[prusaslicer-z-offset-test]: ../img/prusaslicer-z-offset-test.webp
[simplify3d-print-quality-troubleshooting]: https://www.simplify3d.com/resources/print-quality-troubleshooting/
