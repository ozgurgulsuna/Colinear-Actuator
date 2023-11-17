# import required libraries
import cv2
import numpy as np

def perspective_2(img):
    # read the input image

    # find the height and width of image
    # width = number of columns, height = number of rows in image array
    rows,cols,ch = img.shape

    # define four points on input image 476,340 1500,340 1918,643 88,643
    pts1 = np.float32([[476,340],[1500,340],[88,643],[1918,643]])

    # define the corresponding four points on output image
    pts2 = np.float32([[461,484],[1490,470],[461,1080],[1500,1080]])

    # get the perspective transform matrix
    M = cv2.getPerspectiveTransform(pts1,pts2)

    # transform the image using perspective transform matrix
    dst = cv2.warpPerspective(img,M,(cols, rows))
    return dst
