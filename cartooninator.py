import cv2
import numpy as np
import scipy
from matplotlib import pyplot as pp

# Environment Variables

def cartoonify(img):       
    ## Edges
    edges = cv2.Canny(np.uint8(img), 10, 200)
    edges = np.abs(edges - 255)

    # Cartoonization
    color = cv2.bilateralFilter(np.uint8(img), 3, 50, 250)
    img = cv2.bitwise_and(color, color, mask=edges)

    return img

# guassian blur
def blur(img):
    sigma = 10
    G = fgaussian(2 * np.ceil(3 * sigma) + 1, sigma)
    gIm = np.zeros([len(img),len(img[0],3)])
    gIm[0] = scipy.ndimage.convolve(img, G, mode="nearest")
    gIm[1] = scipy.ndimage.convolve(img, G, mode="nearest")
    gIm[2] = scipy.ndimage.convolve(img, G, mode="nearest")
    return gIm
def fgaussian(size, sig):
    
  #Prep for two dims
  shape = (size,size)

  m,n = [(ss-1.)/2. for ss in shape]
  y,x = np.ogrid[-m:m + 1, -n:n + 1]


  h = np.exp( -(x * x + y * y) / (2. * sig * sig) )
  h[ h < np.finfo(h.dtype).eps * h.max() ] = 0

  sumh = h.sum()
  if sumh != 0:
    h /= sumh
  return h

im = pp.imread('images\\cat.jpg')
imgC = cartoonify(im)
pp.imshow(imgC)
pp.show()