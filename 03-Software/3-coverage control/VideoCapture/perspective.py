import cv2 as cv
import math
import numpy as np
#ratio of the points chosen in real life
ratio=1.4
#offsets to make the image bigger(don't you dare to leave it at 0)
offsetW=1050
offsetH=800
def perspective(img):
    pts1 = np.float32([[593 , 479],[1218 , 484],[1365 , 700],[521 , 691]])

    cardH=math.sqrt((pts1[2][0]-pts1[1][0])*(pts1[2][0]-pts1[1][0])+(pts1[2][1]-pts1[1][1])*(pts1[2][1]-pts1[1][1]))
    cardW=ratio*cardH
    pts2 = np.float32([[pts1[0][0],pts1[0][1]], [pts1[0][0]+cardW, pts1[0][1]], [pts1[0][0]+cardW, pts1[0][1]+cardH], [pts1[0][0], pts1[0][1]+cardH]])
    M = cv.getPerspectiveTransform(pts1,pts2)

    transformed = np.zeros((int(cardW+offsetW), int(cardH+offsetH)), dtype=np.uint8)
    dst = cv.warpPerspective(img, M, transformed.shape)
    return dst
