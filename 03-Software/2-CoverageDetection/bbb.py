import cv2 as cv
import numpy as np
img = cv.imread('img.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imshow('res.png',equ)
cv.waitKey(0)