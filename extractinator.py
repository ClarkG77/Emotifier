import numpy as np
import cv2
from matplotlib import pyplot as pp

def objectExtraction(im, coordinates, windowSize, closeIterations=3):
  im = np.uint8(im)

  object = None
  KSize = 3
  dilationCount = 3
  erosionCount = 1

  size = im.shape[0]*im.shape[1]

  if(size < 150*150):
      object = cv2.Canny(im, 10, 200)
      KSize = 2
      dilationCount = 3
      erosionCount = 1
  elif(size >= 150*150 and size < 300*300):
      object = cv2.Canny(im, 30, 150)
      KSize = 4
      dilationCount = 2
      erosionCount = 1

  else:
      object = cv2.Canny(im, 240, 250)


  kernel = np.ones((KSize,KSize), np.uint8)
  object = cv2.dilate(object,kernel,iterations=dilationCount)
  object = cv2.erode(object,kernel,iterations=erosionCount) / 255.0 
  pp.imshow(object)
  pp.show()
  for coord in coordinates:
      object[coord[0],coord[1]] = 2
      object[coord[0] + 1,coord[1]] = 2


      fill = None
      neighborhood = object[coord[0] - 1:coord[0] + 2,coord[1] - 1:coord[1] + 2]
      if np.sum(neighborhood == 1) > np.sum(neighborhood == 0):
          fill = 1
      else:
          fill = 0
      
      coords = [coord]
      while len(coords) != 0:
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


  im = (im - np.min(im))/(np.max(im) - np.min(im))

  for i,row in enumerate(object):
      for j,pixel in enumerate(row):
          if pixel != 2:
              im[i,j] = np.nan
  return im
