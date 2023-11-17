import cv2 as cv
import numpy as np
img = cv.imread('img.jpg',0)
equ = cv.equalizeHist(img)
cv.imshow('equ',equ)
gas = cv.GaussianBlur(img,(5,5),0)
cv.imshow('gauss',gas)
gas_equ = cv.GaussianBlur(equ,(5,5),0)
cv.imshow('gauss ',gas)
cv.waitKey(0)