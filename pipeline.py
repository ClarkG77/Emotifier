from matplotlib import pyplot as pp
import numpy as np
from abstractinator import abstract
from pixelinator import pixelizer
from extractinator import objectExtraction
from cartooninator import cartoonify
from rescalinator import resize

def emojiPipeline(image, coords, type, rmBack, windowSize):
    im = pp.imread(image)
    im = resize(im)
    for i, coord in enumerate(coords):
        coords[i] = (int(coord[0]/4),int(coord[1]/4))

    if type == 'C':
        im = cartoonify(im)

    if rmBack:
        im = objectExtraction(im, coords, 3, 1)

    if type == 'A':
        im[np.isnan(im)] = -1
        im = abstract(im)
        im[im == -1] = np.nan
        if not rmBack:
            im = np.uint8(im)
    elif type == 'P':
        im = pixelizer(im,windowSize)
        if not rmBack:
            im = np.uint8(im)
    return im

pp.imshow(emojiPipeline('images\\mountains.jpg',[(600,700)],'P',False,5))
pp.show()
pp.imshow(emojiPipeline('images\\mountains.jpg',[(600,700)],'P',True,5))
pp.show()

pp.imshow(emojiPipeline('images\\mountains.jpg',[(600,700)],'A',False,5))
pp.show()
pp.imshow(emojiPipeline('images\\mountains.jpg',[(600,700)],'A',True,5))
pp.show()

pp.imshow(emojiPipeline('images\\mountains.jpg',[(600,700)],'C',False,5))
pp.show()
pp.imshow(emojiPipeline('images\\mountains.jpg',[(600,700)],'C',True,5))
pp.show()
    
