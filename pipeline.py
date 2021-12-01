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
    if rmBack:
        im[np.isnan(im)] = 0
        im = resize(im)
        im[im == -1] = np.nan
        pp.imshow(im)
        pp.show()
    else:
        im = resize(im)

    if np.any(im[0]<1) and np.any(im[0]>0):
        im = np.floor(im*255)

    if type == 'C':
        im[np.isnan(im)] = 0
        im = np.uint8(im)
        im = cartoonify(im)

    if rmBack:        

        mins = np.min(im[np.isnan(im) == False])
        max = np.max(im[np.isnan(im) == False])
        im = (im - mins)/(max - mins)


    if type == 'A':
        im[np.isnan(im)] = 0
        im = abstract(im)
        im[im == -1] = np.nan
        if not rmBack:
            im = np.uint8(im)

    elif type == 'P':

        im[np.isnan(im)] = 0
        im = abstract(im)
        im[im == -1] = np.nan
        im = pixelizer(im,windowSize)
        if not rmBack:
            im = np.uint8(im)

    return im
    
