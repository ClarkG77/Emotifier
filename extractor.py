import numpy as np
import matplotlib.pyplot as pp
import cv2
import pixelizer

def objectExtraction(im, coord, windowSize, closeIterations=5):
  object = cv2.Canny(im, 240, 250)
  kernel = np.ones((5,5), np.uint8)
  object = cv2.dilate(object,kernel,iterations=3)
  object = cv2.erode(object,kernel,iterations=1) / 255.0

  object[coord[0],coord[1]] = 2
  object[coord[0] + 1,coord[1]] = 2

  coords = [coord]


  fill = None
  neighborhood = object[coord[0] - 1:coord[0] + 2,coord[1] - 1:coord[1] + 2]
  if np.sum(neighborhood == 1) > np.sum(neighborhood == 0):
      fill = 1
  else:
      fill = 0

  while len(coords) is not 0:
    pixel = coords.pop()

    # Obtain 3x3 neighborhood with pixel in the center
    neighborhood = object[pixel[0] - 1:pixel[0] + 2,pixel[1] - 1:pixel[1] + 2]

    replaced = np.where(neighborhood == fill)

    for i in range(0, len(replaced[0])):
        coords.append((pixel[0] - 1 + replaced[0][i], pixel[1] - 1 + replaced[1][i]))

    neighborhood[neighborhood == fill] = 2

  for iter in range(0,closeIterations):
      for i in range(0, object.shape[0]):
          for j in range(0, object.shape[1]):
              if np.sum(object[i: i + windowSize,j: j + windowSize] == 2) / (windowSize * windowSize) > .87:
                  object[i: i + windowSize, j: j + windowSize] = 2

  return object

#imCat = pp.imread('images\\Eiffel.jpg')
#mid = objectExtraction(imCat,(180,100),3, 1)

#imCat = (imCat - np.min(imCat))/(np.max(imCat) - np.min(imCat))

#for i,row in enumerate(mid):
#    for j,pixel in enumerate(row):
#        if pixel != 2:
#            imCat[i,j] = np.nan
#pp.imshow(imCat) 
#pp.show()
#imPixel = pixelizer.pixelizer(imCat,5)
#pp.imshow(imPixel)
#pp.show()