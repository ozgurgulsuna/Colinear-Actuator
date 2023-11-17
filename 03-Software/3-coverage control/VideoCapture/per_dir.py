import cv2 as cv
import numpy as np
import center
def per_dir(img_base,contb,img_track,contt,shape, third, base,i):   
    base_center=center.center(contb[0],shape)
    track_center=center.center(contt[0],shape)
    img_base.astype('int64')
    img_track.astype('int64')
    if (base_center[0][1]-track_center[0][1])>shape[1]*0.05:
        print("right by ", (base_center[0][1]-track_center[0][1])/shape[1]*100,"%")
    elif(base_center[0][1]-track_center[0][1])<-shape[1]*0.05:
        print("left by ", (track_center[0][1]-base_center[0][1])/shape[1]*100,"%")
    elif (base_center[0][2]-track_center[0][2])>shape[0]*0.05:
        print("down by ", (base_center[0][2]-track_center[0][2])/shape[0]*100,"%")
    elif (base_center[0][2]-track_center[0][2])<-shape[0]*0.05:
        print("up by ", (track_center[0][2]-base_center[0][2])/shape[0]*100,"%")
    # if(0):
    #     pass
    else:
        # print("contb[0][0]: ",len(contb[0][0]))
        if cv.contourArea(contt[0][0])-cv.contourArea(contb[0][0])\
            >cv.contourArea(contb[0][0])*0.05:
            print("go further from light")            # area is larger than base area
            percentage=((cv.contourArea(contt[0][0])-cv.contourArea(contb[0][0]))/cv.contourArea(contb[0][0]))*100
        elif cv.contourArea(contb[0][0])-cv.contourArea(contt[0][0])\
            >cv.contourArea(contb[0][0])*0.05:
            print("close to light")                    # area is smaller than base area
            percentage=((cv.contourArea(contb[0][0])-cv.contourArea(contt[0][0]))/cv.contourArea(contb[0][0]))*100
        else:
            print("A OK!")
            percentage=((cv.contourArea(contt[0][0])-cv.contourArea(contb[0][0]))/cv.contourArea(contb[0][0]))*100
            print("Area error of the system: ",abs(percentage))
            print("Error in the x axis: ", abs(base_center[0][1]-track_center[0][1])/shape[1]*100)
            print("Error in the y axis: ", abs(base_center[0][2]-track_center[0][2])/shape[0]*100)

            cv.imshow('Tracked image found', third)
            cv.imshow('Base Image', base)
            cv.imwrite('VideoCapture\TestImages\Base{}.jpeg'.format(i), base)
            cv.imwrite('VideoCapture\TestImages\Third{}.jpeg'.format(i), third)

            return 1
    return 0        