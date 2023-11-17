import cv2 as cv
import numpy as np
import center
def per_dir(img_base,contb,img_track,contt,shape):   
    base_center=center.center(contb[0],shape)
    track_center=center.center(contt[0],shape)
    img_base.astype('int64')
    img_track.astype('int64')
    if (base_center[0][1]-track_center[0][1])>shape[1]*0.5:
        print("right by ", (base_center[0][1]-track_center[0][1])/shape[1]*100,"%")
    elif(base_center[0][1]-track_center[0][1])<-shape[1]*0.5:
        print("left by ", (track_center[0][1]-base_center[0][1])/shape[1]*100,"%")
    elif (base_center[0][2]-track_center[0][2])>shape[0]*0.5:
        print("down by ", (base_center[0][2]-track_center[0][2])/shape[0]*100,"%")
    elif (base_center[0][2]-track_center[0][2])<-shape[0]*0.5:
        print("up by ", (track_center[0][2]-base_center[0][2])/shape[0]*100,"%")
    else:
        if sum([sum(i) for i in img_track])-sum([sum(i) for i in img_base])\
            >sum([sum(i) for i in img_base])*0.5:
            print("go further from light")            # area is larger than base area
            percentage=((sum([sum(i) for i in img_base])-sum([sum(i) for i in img_track]))/sum([sum(i) for i in img_base]))*100
        elif sum([sum(i) for i in img_track])-sum([sum(i) for i in img_base])\
            <-sum([sum(i) for i in img_base])*0.5:
            print("closer to light")           # area is smaller than base area
            percentage=((sum([sum(i) for i in img_track])-sum([sum(i) for i in img_base]))/sum([sum(i) for i in img_base]))*100
        else:
            print("A OK!")
            percentage=((sum([sum(i) for i in img_track])-sum([sum(i) for i in img_base]))/sum([sum(i) for i in img_base]))*100
            print("Error of the system: ",percentage)

            return 1
    return 0        