import cv2 as cv
import numpy as np
import time
import lir_within_contour as lir


def rect_detect(conts,shape):
    #start = time.time()
    # Import your picture
    # Color it in gray

    # Create our mask by selecting the non-zero values of the picture
    # Select the contour
    # if your mask is incurved or if you want better results, 
    # you may want to use cv2.CHAIN_APPROX_NONE instead of cv2.CHAIN_APPROX_SIMPLE, 
    # but the rectangle search will be longer
    recto=[]
    blank=np.zeros(shape,dtype="uint8")
    for x in conts:
        mask = np.zeros(shape, dtype='uint8')

        contour = x[0][:, 0, :]

        # print(contour)
        cv.drawContours(mask, x, -1, 255, -1)
        grid=mask>0
        cv.imshow("mask", (grid*255).astype("uint8"))
        rect=lir.largest_interior_rectangle(grid,contour)
        # print(rect)
        cv.rectangle(blank,[rect[0],rect[1]],[rect[2]+rect[0],rect[3]+rect[1]],255,-1)
        recto.append([rect])

    #cv.imshow("Rectangle detected image", blank)
    #end = time.time()
    # print(end - start)
    #cv.waitKey(0)
    return blank, rect

    