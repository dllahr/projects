import numpy
import os.path


scaling = 0.8


f = open("png_brightness.grp")
brightness = [float(x) for x in f.read().strip().split("\n")]
f.close()


f = open("ordered_png_snapshots.grp")
pngs = [os.path.basename(x) for x in f.read().strip().split("\n")]
f.close()


ave = numpy.mean(brightness)


adjustments = [100.0*scaling*ave/x for x in brightness]

output_lines = [pngs[i] + ("\t%.0f" % x) for (i, x) in enumerate(adjustments)]

f = open("png_snapshot_and_brightness_adjustment2.txt", "w")
f.write("\n".join(output_lines) + "\n")
f.close()
