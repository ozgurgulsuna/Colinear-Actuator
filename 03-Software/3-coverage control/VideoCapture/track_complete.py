import numpy as np
import cv2 as cv

def track_complete(src_cont, intersect_img):
    tracked_img=np.ones(intersect_img.shape, dtype='uint8')*255

    for cont in src_cont:
        blank=np.ones(intersect_img.shape, dtype='uint8')*255
        cv.drawContours(blank, cont, -1, 0, -1)

        bitwise_and = cv.bitwise_and(blank, intersect_img)
        contours, _ = cv.findContours(bitwise_and, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        if(len(contours) != 0):
            cv.drawContours(tracked_img, cont, -1, 0, -1)
            cv.imshow('Tracked image', tracked_img)
            break


    return [cont], tracked_img