import cv2 as cv
import numpy as np
from rect_corner_detect import *
import time
start = time.time()

# Read image 
img = cv.imread('untitled2.png', cv.IMREAD_COLOR) # road.png is the filename
# Convert the image to gray-scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
shape=gray.shape
# Find the edges in the image using canny detector
gray = cv.bilateralFilter(gray, 0, 100, cv.BORDER_DEFAULT)

_, threshold = cv.threshold(gray, 127, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

blank= np.ones([img.shape[0],img.shape[1]], dtype='uint8')*255
contour_lists=[]
t=0
for i in contours:
    if t==0:
        t=1
        continue
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    tlist=(i,cx,cy)
    contour_lists.append(tlist)
    t=t+1

print('hi')
cv.drawContours(blank, contour_lists[0], 0, color=(0, 0, 0), thickness=cv.FILLED)

corners=get_rectangle_coordinates(blank/255)
area=0
print(corners)
for i in range(len(corners)):
    if area<(corners[i][2]-corners[i][0]+1)*(corners[i][3]-corners[i][1]+1):
        area=(corners[i][2]-corners[i][0]+1)*(corners[i][3]-corners[i][1]+1)
        cor1=[corners[i][1],corners[i][0]]
        cor2=[corners[i][3],corners[i][2]]
        print('hey')

blank = np.zeros(shape, dtype='uint8')
cv.rectangle(blank, cor1, cor2, color=(255, 255, 255), thickness=cv.FILLED)


cv.imshow('hi',blank.astype("uint8"))
cv.imwrite('hi.png',blank.astype("uint8"))
end = time.time()
print(end - start)
cv.waitKey(0)


