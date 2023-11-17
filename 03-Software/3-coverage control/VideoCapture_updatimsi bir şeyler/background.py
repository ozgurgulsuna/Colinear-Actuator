import os 
import numpy as np
import cv2

def background():
    cap = cv2.VideoCapture('http://192.168.3.166:8080/video')
    i=1
    while(True):
        _ , back = cap.read()
        cv2.imshow('Live Video', cv2.resize(back,(int(back.shape[1]*0.75),int(back.shape[0]*0.75)),interpolation=cv2.INTER_AREA))
        pressed = cv2.waitKey(1) & 0xFF
        if (pressed == ord('2')):
            cv2.imwrite('C:/Users/Furkan/Desktop/back/Back{}.jpeg'.format(i), back) #######directorrrrrry
            i=i+1
        if (i == 8):
            break
        
    # cap = cv2.VideoCapture(0)

    ##############################################
    # get the path/directory
    folder_dir = "C:/Users/Furkan/Desktop/back" #######directorrrrrry
    frames = []
    for fid in os.listdir(folder_dir):
        
        if (fid.endswith(".jpeg")):
            cap=cv2.imread("C:/Users/Furkan/Desktop/back/"+fid, cv2.IMREAD_COLOR) #######directorrrrrry
            frames.append(cap)

    # Calculate the median along the time axis
    medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)  
    return medianFrame  

