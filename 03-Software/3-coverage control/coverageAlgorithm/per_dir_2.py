import cv2 as cv
import numpy as np
def per_dir(shape,rect_points):
    #### base_ratio===ekranda görünmesi gereken yerin x/y oranı
    base_ratio=60/45   ##değiştirilecek
    err=0.05
    ((rect_points[2])/2).astype(np.uint32)
    if (((rect_points[2])/2)+rect_points[0]-shape[1]/2)>shape[1]*err:
        print("right by ", (((rect_points[2])/2)+rect_points[0]-shape[1]/2)/shape[1]*100,"%")
    elif (((rect_points[2])/2)+rect_points[0]-shape[1]/2)<-shape[1]*err:
        print("left by ", (shape[1]/2-((rect_points[2])/2)-rect_points[0])/shape[1]*100,"%")
    else:
        print("Stop x")
    
    
    if rect_points[2]/rect_points[3] > base_ratio+base_ratio*err:
        print("up by ", (rect_points[2]/base_ratio-rect_points[3])/shape[0]*100,"%")
    elif rect_points[2]/rect_points[3] < base_ratio-base_ratio*err:
        print("down by ", -1*(rect_points[2]/base_ratio-rect_points[3])/shape[0]*100,"%")
    else:
        print("Stop y")
    
