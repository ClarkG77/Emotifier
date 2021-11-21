import numpy as np
import matplotlib.pyplot as pp
import cv2

def objectExtraction(im, coord, windowSize, closeIterations=5):
  object = cv2.Canny(im, 240, 250)
  kernel = np.ones((5,5), np.uint8)
  object = cv2.dilate(object,kernel,iterations=3)
  object = cv2.erode(object,kernel,iterations=1) / 255.0

  object[coord[0],coord[1]] = 2
  object[coord[0] + 1,coord[1]] = 2

  coords = [coord]

  while len(coords) is not 0:
    pixel = coords.pop()

    # Obtain 3x3 neighborhood with pixel in the center
    neighborhood = object[pixel[0] - 1:pixel[0] + 2,pixel[1] - 1:pixel[1] + 2]

    replaced = np.where(neighborhood == 0)

    for i in range(0, len(replaced[0])):
        coords.append((pixel[0] - 1 + replaced[0][i], pixel[1] - 1 + replaced[1][i]))

    neighborhood[neighborhood == 0] = 2

  for iter in range(0,closeIterations):
      for i in range(0, object.shape[0]):
          for j in range(0, object.shape[1]):
              if np.sum(object[i: i + windowSize,j: j+windowSize] == 2) / (windowSize * windowSize) > .87:
                  object[i: i + windowSize, j: j + windowSize] = 2

  return object

imCat = pp.imread('images\\cat.jpg')
mid = objectExtraction(imCat,(330,530),3, 1)
pp.imshow(mid)
pp.show()