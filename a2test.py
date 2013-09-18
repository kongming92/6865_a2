from a2 import *
import imageIO as io
import numpy as np
import math

panda = io.imread("panda2.png")
bear = io.imread("bear.png")
fredo = io.imread("fredo2.png")
werewolf = io.imread("werewolf.png")

# Test scaling
io.imwrite(scaleNN(panda, 2.5), "pandaNN_2.5.png")
io.imwrite(scaleNN(panda, 0.5), "pandaNN_0.5.png")
io.imwrite(scaleLin(panda, 2.5), "pandaLin_2.5.png")
io.imwrite(scaleLin(panda, 0.5), "pandaLin_0.5.png")
io.imwrite(scaleLin(fredo, 2.5), "fredoLin_2.5.png")
io.imwrite(scaleLin(fredo, 0.5), "fredoLin_0.5.png")

# Test rotation
io.imwrite(rotate(panda, math.pi / 4), "pandaRotate45.png");
io.imwrite(rotate(panda, math.pi / 2), "pandaRotate90.png");
io.imwrite(rotate(panda, math.pi), "pandaRotate180.png");
io.imwrite(rotate(fredo, math.pi / 6), "fredoRotate30.png");

# Test warp single segment
io.imwrite(warpBy1(bear, segment(0,0, 10,0), segment(10, 10, 30, 15)), "bearWarpBy1.png")

# Test warp 2 segments
segmentsBefore=np.array([segment(13, 10, 50, 10), segment(119, 72, 119, 28)])
segmentsAfter=np.array([segment(8, 12, 38, 34), segment(117, 71, 91, 36)])
io.imwrite(warp(bear, segmentsBefore, segmentsAfter), "bearWarp2.png")

# Test morph
segmentsBefore=np.array([segment(11, 37, 37, 20), segment(149, 35, 175, 79), segment(88, 130, 110, 128), segment(146, 129, 163, 132), segment(104, 198, 130, 190), segment(126, 220, 136, 197), segment(41, 197, 70, 249), segment(140, 237, 164, 170)])
segmentsAfter=np.array([segment(12, 45, 32, 18), segment(160, 16, 177, 56), segment(83, 114, 105, 112), segment(142, 106, 158, 105), segment(103, 170, 131, 155), segment(126, 196, 144, 175), segment(79, 174, 100, 216), segment(145, 194, 157, 139)])
results = morph(fredo, werewolf, segmentsBefore, segmentsAfter, 5)
for i, im in enumerate(results):
	io.imwrite(im, "morph" + str(i) + ".png")