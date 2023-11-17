import cv2 as cv
import numpy as np
par1=int(input('parameter 1: '))
par2=int(input('parameter 2: '))
par3=int(input('parameter 3: '))

blank = np.zeros((800,800), dtype='uint8')#playfield
cv.imshow('blank',(blank))
canopy = cv.rectangle(blank.copy(), (40,40), (140,140), 255, -1)
cv.imshow('canopy',canopy)



cv.waitKey(0)

################################################################
################################################################