import a2
import imageIO as io
import math

image = io.imread("panda2.png")
io.imwrite(a2.scaleNN(image, 2.5), "pandaNN.png")
io.imwrite(a2.scaleLin(image, 2.5), "pandaLin.png")
io.imwrite(a2.rotate(image, math.pi / 4), "pandaRotate.png");

image = io.imread("bear.png")
io.imwrite(a2.warpBy1(image, a2.segment(0,0, 10,0), a2.segment(10, 10, 30, 15)), "bearWarp.png")