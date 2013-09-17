from a2 import *
import imageIO as io
import numpy as np
import math

image = io.imread("panda2.png")
io.imwrite(scaleNN(image, 2.5), "pandaNN.png")
io.imwrite(scaleLin(image, 2.5), "pandaLin.png")
io.imwrite(rotate(image, math.pi / 4), "pandaRotate.png");

image = io.imread("bear.png")
io.imwrite(warpBy1(image, segment(0,0, 10,0), segment(10, 10, 30, 15)), "bearWarp.png")

image = io.imread("bear.png")
segmentsBefore=np.array([segment(13, 10, 50, 10), segment(119, 72, 119, 28)])
segmentsAfter=np.array([segment(8, 12, 38, 34), segment(117, 71, 91, 36)])
io.imwrite(warp(image, segmentsBefore, segmentsAfter), "bearWarp2.png")

im1 = io.imread("fredo2.png")
im2 = io.imread("werewolf.png")
segmentsBefore=np.array([segment(11, 37, 37, 20), segment(149, 35, 175, 79), segment(88, 130, 110, 128), segment(146, 129, 163, 132), segment(104, 198, 130, 190), segment(126, 220, 136, 197), segment(41, 197, 70, 249), segment(140, 237, 164, 170)])
segmentsAfter=np.array([segment(12, 45, 32, 18), segment(160, 16, 177, 56), segment(83, 114, 105, 112), segment(142, 106, 158, 105), segment(103, 170, 131, 155), segment(126, 196, 144, 175), segment(79, 174, 100, 216), segment(145, 194, 157, 139)])
images, beforemorph, aftermorph = morph(im1, im2, segmentsBefore, segmentsAfter)
for i, im in enumerate(images):
	io.imwrite(im, "morph" + str(i) + ".png")
for i, im in enumerate(beforemorph):
	io.imwrite(im, "before" + str(i) + ".png")
for i, im in enumerate(aftermorph):
	io.imwrite(im, "after" + str(i) + ".png")