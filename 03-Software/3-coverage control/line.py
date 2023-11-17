import cv2 as cv
import numpy as np
# Read image 
img = cv.imread('D:\Desktop\GITHUB\Engineering-Design\03-Software\3-coverage control\image comparison\WhatsApp Image 2022-12-16 at 16.46.15.jpeg', cv.IMREAD_COLOR) # road.png is the filename
# Convert the image to gray-scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
gray = cv.bilateralFilter(gray, 0, 100, cv.BORDER_DEFAULT)

edges = cv.Canny(gray, 50, 200)
cv.imshow("aa", edges)
# Detect points that form a line
lines = cv.HoughLinesP(edges, 10, np.pi/180, 200, minLineLength=10, maxLineGap=250)
# Draw lines on the image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
# Show result
cv.imshow("Result Image", img)
cv.waitKey(0)
