from a2 import morph, segment
import numpy as np
import imageIO as io

me = io.imread("classMorph_43.png")
next = io.imread("classMorph_44.png")

segmentsBefore=np.array([segment(65, 120, 83, 119), segment(113, 121, 132, 121), segment(60, 106, 85, 100), segment(110, 104, 137, 108), segment(55, 93, 86, 65), segment(121, 71, 146, 95), segment(87, 168, 113, 166)])
segmentsAfter=np.array([segment(68, 114, 92, 114), segment(116, 114, 134, 114), segment(67, 99, 90, 100), segment(115, 102, 135, 100), segment(62, 79, 92, 63), segment(124, 63, 139, 87), segment(83, 154, 118, 156)])
results = morph(me, next, segmentsBefore, segmentsAfter, 13)
for i, im in enumerate(results):
	io.imwrite(im, "classMorph_43_%(n)02d.png" % {"n" : i})