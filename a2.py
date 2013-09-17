#a2.py
import numpy as np
import math
import imageIO as io


#this file should only contain function definitions.
#It should not call the functions or perform any test.
#Do this in a separate file.

def check_my_module():
   ''' Fill your signature here. When upload your code, check if the signature is correct'''
   my_signature='Charles Liu'
   return my_signature

# HELPER FUNCTIONS AS DEFINED IN CLASS
def imIter(im):
    for y in range(0,im.shape[0]):
        for x in range(0,im.shape[1]):
            yield (y,x)

def getBlackPadded(im, y, x):
    if (x<0) or (x>=im.shape[1]) or (y<0) or (y>= im.shape[0]):
        return np.array([0, 0, 0])
    else:
        return im[y, x]

def clipX(im, x):
    return min(im.shape[1] - 1, max(x, 0))

def clipY(im, y):
    return min(im.shape[0] - 1, max(y, 0))

def getSafePix(im, y, x):
    return im[clipY(im, y), clipX(im, x)];

# END HELPER FUNCTIONS

def pix(im, y, x, repeatEdge=False):
    '''takes an image, y and x coordinates, and a bool
        returns a pixel.
        If y,x is outside the image and repeatEdge==True , you should return the nearest pixel in the image
        If y,x is outside the image and repeatEdge==False , you should return a black pixel
    '''
    return getSafePix(im, y, x) if repeatEdge else getBlackPadded(im, y, x)

def scaleNN(im, k):
    '''Takes an image and a scale factor. Returns an image scaled using nearest neighbor interpolation.
    '''
    out = io.constantIm(im.shape[0] * k, im.shape[1] * k, 0)
    for y, x in imIter(out):
        origY = clipY(im, int(round(y/k)))
        origX = clipX(im, int(round(x/k)))
        out[y, x] = im[origY, origX]

    return out

def interpolateLin(im, y, x, repeatEdge=False):
    '''takes an image, y and x coordinates, and a bool
        returns the interpolated pixel value using bilinear interpolation
    '''
    x0 = int(math.floor(x))
    x1 = int(math.ceil(x))
    y0 = int(math.floor(y))
    y1 = int(math.ceil(y))

    if x0 == x1:
        temp0 = pix(im, y0, x0, repeatEdge)
        temp1 = pix(im, y1, x0, repeatEdge)
    else:
        # Interpolate between x's at y = y0
        temp0 = (x1 - x) * pix(im, y0, x0, repeatEdge) + (x - x0) * pix(im, y0, x1, repeatEdge)
        # Interpolate between x's at y = y1
        temp1 = (x1 - x) * pix(im, y1, x0, repeatEdge) + (x - x0) * pix(im, y1, x1, repeatEdge)

    if y0 == y1:
        return temp0
    # Otherwise, interpolate between y's
    return (y1 - y) * temp0 + (y - y0) * temp1

def scaleLin(im, k, repeatEdge=False):
    '''Takes an image and a scale factor. Returns an image scaled using bilinear interpolation.
    '''
    out = io.constantIm(im.shape[0] * k, im.shape[1] * k, 0)
    for y, x in imIter(out):
        out[y, x] = interpolateLin(im, float(y)/k, float(x)/k, repeatEdge)
    return out

def rotate(im, theta):
    '''takes an image and an angle in radians as input
        returns an image of the same size and rotated by theta
    '''
    out = io.constantIm(im.shape[0], im.shape[1], 0)
    halfX = int(im.shape[1] / 2)
    halfY = int(im.shape[0] / 2)
    inverseRotateM = np.array([[math.cos(theta), -math.sin(theta)],
                               [math.sin(theta), math.cos(theta)]])
    for y, x in imIter(out):
        origImgPos = np.dot(inverseRotateM, np.array([x - halfX, y - halfY])) + np.array([halfX, halfY])
        out[y, x] = interpolateLin(im, origImgPos[1], origImgPos[0])
    return out

class segment:
    def __init__(self, x1, y1, x2, y2):
        #notice that the ui gives you x,y and we are storing as y,x
        self.P=np.array([y1, x1], dtype=np.float64)
        self.Q=np.array([y2, x2], dtype=np.float64)
        #You can precompute more variables here
        #...


    def uv(self, X):
        '''Take the (y,x) coord given by X and return u, v values
        '''
        return u, v

    def dist (self, X):
        '''returns distance from point X to the segment (pill shape dist)
        '''

    def uvtox(self,u,v):
        '''take the u,v values and return the corresponding point (that is, the np.array([y, x]))
        '''



def warpBy1(im, segmentBefore, segmentAfter):
    '''Takes an image, one before segment, and one after segment.
        Returns an image that has been warped according to the two segments.
    '''


def weight(s, X):
    '''Returns the weight of segment s on point X
    '''

def warp(im, segmentsBefore, segmentsAfter, a=10, b=1, p=1):
    '''Takes an image, a list of before segments, a list of after segments, and the parameters a,b,p (see Beier)
    '''


def morph(im1, im2, segmentsBefore, segmentsAfter, N=1, a=10, b=1, p=1):
    '''Takes two images, a list of before segments, a list of after segments, the number of morph images to create, and parameters a,b,p.
        Returns a list of images morphing between im1 and im2.
    '''
    sequence=list()
    sequence.append(im1.copy())
    #add the rest of the morph images
    return sequence