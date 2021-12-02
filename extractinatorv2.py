import numpy as np
import cv2
from matplotlib import pyplot as pp

def objectExtraction(im, coordinates, closeIterations):
	im = np.uint8(im)
	windowSize = 5

	object = None
	KSize = 5
	dilationCount = 3
	erosionCount = 2
	object = cv2.Canny(im, 75, 225)
	size = im.shape[0]*im.shape[1]
	if size >= 1920 * 1080:
		dilationCount = 4
		erosionCount = 2

	
	kernel = np.ones((KSize,KSize), np.uint8)
	object = cv2.dilate(object,kernel,iterations=dilationCount)
	object = cv2.erode(object,kernel,iterations=erosionCount) / 255.0


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
			replaced = None
			tempNeighborhood = np.isin(neighborhood, np.abs(fill - 1))
			if not np.any(tempNeighborhood):
				replaced = np.where(neighborhood == fill)

			if(replaced != None):
				for i in range(0, len(replaced[0])):
					coords.append((pixel[0] - 1 + replaced[0][i], pixel[1] - 1 + replaced[1][i]))

				neighborhood[neighborhood == fill] = 2


	for iter in range(0,closeIterations):
		replace = np.where(object == 2)
		for i in range(0, len(replace[0])):
			object[replace[0][i] - windowSize : replace[0][i] + windowSize, replace[1][i] - windowSize : replace[1][i] + windowSize] = 3
		object[object == 3] = 2

	im = np.float64(im)
	for i,row in enumerate(object):
		for j,pixel in enumerate(row):
			if pixel != 2 and pixel != 3:
				im[i,j] = np.nan
	return im


#pp.imshow(objectExtraction(pp.imread("images\Eiffel.jpg"),[(189,100)],0))
#pp.show()

#pp.imshow(objectExtraction(pp.imread("images\cat.jpg"),[(345,545),(185,670),(230,620),(181,447)],15))
#pp.show()

#pp.imshow(objectExtraction(pp.imread("images\ghost.jpg"),[(325,905),(255,755),(370,680),(530,830),(218,974)], 5))
#pp.show()