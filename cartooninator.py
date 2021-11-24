import cv2
import numpy as np
from skimage.segmentation import slic
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

    return img