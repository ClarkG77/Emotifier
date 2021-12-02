from matplotlib import pyplot as pp
import numpy as np
from abstractinator import abstract
from pixelinator import pixelizer
from extractinatorv2 import objectExtraction
from cartooninator import cartoonify
from rescalinator import resize


def emojiPipeline(image, coords, type, rmBack, windowSize, closeIterations, superpixels):

    im = pp.imread(image)
    if rmBack:
        im = objectExtraction(im, coords, closeIterations)
    if rmBack:
        im[np.isnan(im)] = 0
        im = resize(im)
        im[im == 0] = np.nan

    else:
        im = resize(im)

    if type == 'C':
        if rmBack:
            im[np.isnan(im)] = 0
            im = np.uint8(im)
            im = np.float64(cartoonify(im))
            im[im == 0] = np.nan
        else:
            im = cartoonify(im)

    if rmBack:        

        mins = np.min(im[np.isnan(im) == False])
        max = np.max(im[np.isnan(im) == False])
        im = (im - mins)/(max - mins)


    if type == 'A':
        im[np.isnan(im)] = 0
        im = abstract(im,superpixels)
        im[im == 0] = np.nan
        if not rmBack:
            im = np.uint8(im)

    elif type == 'P':

        im[np.isnan(im)] = 0
        im = pixelizer(im,windowSize)
        im[im == 0] = np.nan
        if not rmBack:
            im = np.uint8(im)

    return im
    
