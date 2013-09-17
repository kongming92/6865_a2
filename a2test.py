import a2
import imageIO as io
import math

image = io.imread("panda2.png")
'''
out = a2.scaleNN(image, 2.5)
io.imwrite(out, "NN.png")
out = a2.scaleLin(image, 2.5)
io.imwrite(out, "Lin.png")'''
out = a2.rotate(image, math.pi / 4)
io.imwrite(out, "rotate.png");