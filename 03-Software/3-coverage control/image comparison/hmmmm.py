import cv2 as cv
import numpy as np
first = cv.imread("image comparison/first.jpeg", 0)
second = cv.imread("image comparison/second.jpeg", 0)
first = cv.GaussianBlur(first,(5,5),0)
second = cv.GaussianBlur(second,(5,5),0)
#
print(np.mean(first))

mask = cv.inRange(second, 0, np.mean(second))
cv.imshow("mask", mask)
print(np.mean(second))


#
diff=(first-second)
diff=cv.absdiff(first,second)
#// inorder to perform the absdiff, the images need to be of equal size
#// NOTE: I believe this is the reason why you have a big blue box on the edges
#// as well of the output image. This can be fixed by using two equal images in the first place


#// after getting the difference, we binarize it

_,thresh=cv.threshold(diff, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
con_real=[]
t=0
print(type(cv.mean(second,mask = mask)[0]))
for cont in contours:
    if t==0:
        t+=1
        continue
    mask = np.zeros(second.shape,np.uint8)
    cv.drawContours(mask,[cont],0,255,-1)
    if cv.contourArea(cont)>50000 and np.mean(second) > cv.mean(second,mask = mask)[0]:
        con_real.append(cont)
blank=np.ones(first.shape, dtype='uint8')*255
cv.drawContours(blank, con_real, -1, (0,0,0), -11)
cv.imshow('Contours Drawn', blank)
cv.imwrite('aaa.png',blank)
#// this matrix will be used for drawing purposes
out=cv.cvtColor(second, cv.COLOR_GRAY2BGR)


#// For each detected contour, calculate its bounding rectangle and draw it
#// You can also filter out some noise should you wish by checking if the contour is big
#// or small enough along with other contour properties.
#// Ref: https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
#// Ref: https://docs.opencv.org/trunk/d1/d32/tutorial_py_contour_properties.html
for cont in con_real:
    box = cv.boundingRect(cont)
    cv.rectangle(out, box,(255, 0, 0))




cv.waitKey(0)
