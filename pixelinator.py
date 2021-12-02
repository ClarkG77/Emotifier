import numpy as np
def pixelizer(im, windowSize):
    pixelized = np.zeros(im.shape)
    for i in range(0, im.shape[0], windowSize):
        for j in range(0, im.shape[1], windowSize):
            pixelized[i:i + windowSize,j:j + windowSize,0] = np.sum(im[i:i + windowSize,j:j + windowSize,0]) / (windowSize * windowSize)
            pixelized[i:i + windowSize,j:j + windowSize,1] = np.sum(im[i:i + windowSize,j:j + windowSize,1]) / (windowSize * windowSize)
            pixelized[i:i + windowSize,j:j + windowSize,2] = np.sum(im[i:i + windowSize,j:j + windowSize,2]) / (windowSize * windowSize)

    return pixelized