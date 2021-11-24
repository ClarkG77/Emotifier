# importing libraries
import numpy as np
from skimage.segmentation import slic


# Environment Variables
SUPERPIXELS = 1000
SIGMA = 0
COMPACTNESS = .1

def abstract(img):    
    superpixels = slic(img, n_segments = SUPERPIXELS, sigma = SIGMA,compactness=COMPACTNESS)
    # go through every pixel in superpixels and average them from the image should be able to splice 
    for numSegements in range(SUPERPIXELS):
        indecies = np.where(superpixels == numSegements)
        img[indecies[0],indecies[1],0] = np.average(img[indecies[0],indecies[1],0])
        img[indecies[0],indecies[1],1] = np.average(img[indecies[0],indecies[1],1])
        img[indecies[0],indecies[1],2] = np.average(img[indecies[0],indecies[1],2])

    return img
