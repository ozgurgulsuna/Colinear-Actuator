##center coordinates of a shape
import cv2 as cv
import numpy as np
def center(contours,shape):

    contour_lists=[]

    for i in contours:
        if cv.contourArea(i) < ((shape[0]-1)*(shape[1]-1)):
            M = cv.moments(i)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            tlist=(i,cx,cy)
            contour_lists.append(tlist)
    return contour_lists
