import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as pp

# Environment Variables

def cartoonify(img):       
    ## Edges
    edges = cv2.Canny(np.uint8(img), 10, 200)
    edges = np.abs(edges - 255)

    # Cartoonization
    color2 = blur(np.uint8(img))
    img = cv2.bitwise_and(color2, color2, mask=edges)

    return img

# guassian blur
def blur(img):
    sigma = 3
    G = fgaussian(2 * np.ceil(3 * sigma) + 1, sigma)
    gIm = np.uint8(np.zeros([len(img),len(img[0]),3]))
    gIm[:,:,0] = ndimage.convolve(img[:,:,0], G, mode="nearest")
    gIm[:,:,1] = ndimage.convolve(img[:,:,1], G, mode="nearest")
    gIm[:,:,2] = ndimage.convolve(img[:,:,2], G, mode="nearest")
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