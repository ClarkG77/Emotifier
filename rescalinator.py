import cv2
import numpy as np

#blur takes in an 'a' and outputs a mask.
def fblur(a):
  return np.array([.25-.5*a, .25, a, .25, .25-.5*a])

# sample an array for every other value. 
def sample(array2D):
  sampled = array2D[::2,::2]
  return sampled

def interpolate(array2D):
  m,n = array2D.shape

  n = 2 * n - 1
  m = 2 * m - 1

  interp = np.zeros((m,n))
  interp[::2,::2] = array2D


  avgCol = (interp[::2, 0:n-1:2] + interp[::2, 2::2]) / 2
  avgRow = (interp[0:m-1:2, ::2] + interp[2::2, ::2]) / 2
  diagLR = interp[:m-1:2, 0:n-1:2] + interp [2::2, 2::2]
  diagRL = interp[:m-1:2, 2::2] + interp[2::2, 0:n-1:2]
  avgMid = ( diagLR + diagRL ) / 4 # this is getting diagnals
  interp[::2, 1::2] = avgCol
  interp[1::2, ::2] = avgRow
  interp[1::2, 1::2] = avgMid
  return interp

def rescale(im):
    imSampled = {}
    imSampled[0] = im

    for N in range(1,4):
      gauss = fblur(.4)
      imBlur = cv2.sepFilter2D(imSampled[N - 1], -1, gauss, gauss)
      imSampled[N] = sample(imBlur)

    #get that interp array
    imInterp = {}
    for N in range(1,4):
      imInterp[4-N] = interpolate(imSampled[4-N])

    # mmm Error Time
    N = 3
    imError = imSampled[N - 1] - imInterp[N]

    imSent = imSampled[3]

    imsInterp = interpolate(imSent)
    return imsInterp + imError

def resize(im):
    overRow = (im.shape[0] - 1) % 16
    overCol = (im.shape[1] - 1) % 16
    im = im[0:im.shape[0] - overRow,0:im.shape[1] - overCol,:]

    smolR = rescale(im[:,:,0])
    smolG = rescale(im[:,:,1])
    smolB = rescale(im[:,:,2])

    smol = np.zeros((smolR.shape[0],smolR.shape[1],3))

    smol[:,:,0] = smolR
    smol[:,:,1] = smolG
    smol[:,:,2] = smolB
    return smol

