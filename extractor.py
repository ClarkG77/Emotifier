import numpy as np
import matplotlib.pyplot as pp
import cv2

def objectExtraction(im, coord):
  object = cv2.Canny(im, 240, 250)
  kernel = np.ones((5,5), np.uint8)
  object = cv2.dilate(object,kernel,iterations=3)
  object = cv2.erode(object,kernel,iterations=1) / 255.0

  object[coord[0],coord[1]] = 2
  object[coord[0] + 1,coord[1]] = 2

  numChanged = 1
  epoch = 0
  while numChanged != 0:

    #if epoch % 100 == 0:
    #  pp.figure()
    #  pp.title(epoch)
    #  pp.imshow(object)
    #  pp.show()

    numChanged = 0
    epoch += 1

    #Find all twos.
    twoLocs = np.where(object == 2)
    twos = np.zeros((len(twoLocs[0]),2),dtype=np.int16)
    for i in range(0,twos.shape[0]):
        twos[i,0] = twoLocs[0][i]
        twos[i,1] = twoLocs[1][i]

    for pixel in twos:          
        # Obtain 3x3 neighborhood with pixel in the center
        neighborhood = object[pixel[0] - 1:pixel[0] + 2,pixel[1] - 1:pixel[1] + 2]
        numChanged += np.sum(neighborhood == 0)
        neighborhood[neighborhood == 0] = 2

  return object

imCat = pp.imread('images\\cat.jpg')
mid = objectExtraction(imCat,(330,530))
pp.imshow(mid)
pp.show()