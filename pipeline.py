from matplotlib import pyplot as pp
import numpy as np
from abstractinator import abstract
from pixelinator import pixelizer
from extractinatorv2 import objectExtraction
from cartooninator import cartoonify
from rescalinator import resize


def emojiPipeline(image, coords, type, rmBack, windowSize, closeIterations):

    im = pp.imread(image)
    if rmBack:
        im = objectExtraction(im, coords, closeIterations)

    im = resize(im)
    if np.any(im[0]<1) and np.any(im[0]>0):
        im = np.floor(im*255)
    for i, coord in enumerate(coords):
        coords[i] = (int(coord[0]/4),int(coord[1]/4))

    if type == 'C':
        im = np.int32(im)
        im = cartoonify(im)

    if type == 'A':
        im[np.isnan(im)] = -1
        im = abstract(im)
        im[im == -1] = np.nan
        if not rmBack:
            im = np.uint8(im)
        else:
            im = (im - np.min(im))/(np.max(im) - np.min(im))

    elif type == 'P':
        im = pixelizer(im,windowSize)
        if not rmBack:
            im = np.uint8(im)
        else:
            im = (im - np.min(im))/(np.max(im) - np.min(im))

    return im
    
