import cv2
import numpy as np
from skimage.segmentation import slic
import matplotlib.pyplot as plt

# Environment Variables

def cartoonify(img):       
    # Edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                            cv2.THRESH_BINARY, 9, 9)
    
    # Cartoonization
    color = cv2.bilateralFilter(img, 9, 250, 250)
    img = cv2.bitwise_and(color, color, mask=edges)

    return img

# guassian blur
def blur(img):

    return img
# img = cv2.imread('images\\Eiffel.jpg')
img = cv2.imread('images\\cat.jpg')
# img = cv2.imread('images\\person.jpg')
#img = cv2.imread('images\\Poro King.jpg')
cv2.imshow("Image", img)
cartoon = cartoonify(img)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)