# import the opencv library
import cv2
import img_compare
import rect_detect
import track_complete
import math
import perspective
import center
import per_dir as per_dir
import background


def rescaleFrame(frame, scale = 0.75):
    #images,videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)


# define a video capture object

# 0 : webcam, to find other cameras, change the number
#vid = cv2.VideoCapture(0)

# IP Webcam app (Play Store)
vid = cv2.VideoCapture('http://192.168.137.206:8080/video')


# first, second and base images to compare, in case no pictures is taken for comparison
ret, first = vid.read()
first = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
first = rescaleFrame(first, 0.6)
base = first
second = first

i = 0               # only for saving images
########################################################################################################
first=background.background()#### check the directory <------------------------------------------------

while(True):
    # Capture the video frame by frame
    ret, frame = vid.read()

    # to find a working channel, added
    # print('Is camera is available? ',ret)

    # for ip based camera, scale is needed to obtain videos that fits to the screen
    frame = rescaleFrame(frame, 0.6)

    # Display the resulting frame
    cv2.imshow('Live Video', frame)

    pressed = cv2.waitKey(1) & 0xFF
    # pressed button
    if ((pressed == ord('f')) or (pressed == ord('s')) or (pressed == ord('t')) or (pressed == ord('b')) or (pressed == ord('q')) or (pressed == ord('d'))):
        # capture first image for comparison
        # waits 1 msec
        if pressed == ord('f'):
            ret, first = vid.read()
            first = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
            first = rescaleFrame(first, 0.6)
            #first = perspective.perspective(first)
            print(first.shape)

            # Display the resulting frame
            cv2.imshow('First', first)
            cv2.imwrite('VideoCapture\TestImages\ClearImage.jpeg', first)
    
        # capture second image
        elif pressed == ord('s'):
            # send this frame to the image processing algorithm
            ret, second = vid.read()
            second = rescaleFrame(second, 0.6)
            #second = perspective.perspective(second)

            # Display the resulting frame
            cv2.imshow('Second', second)
            second = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)
            cont12, cont12_img = img_compare.img_compare(first, second)
            # points_sec=rect_detect.rect_detect(cont,second.shape)

            cv2.imwrite('VideoCapture\TestImages\Shadow{}.jpeg'.format(i), first)
            i = i + 1

        elif pressed == ord('t'):
            # send this frame to the image processing algorithm
            ret, third = vid.read()
            third = rescaleFrame(third, 0.6)
            #third = perspective.perspective(third)

            # Display the resulting frame
            cv2.imshow('Third', third)
            third = cv2.cvtColor(third, cv2.COLOR_BGR2GRAY)
            cont13, cont13_img = img_compare.img_compare(first, third)

            cont23, cont23_img = img_compare.img_compare(second, third)                     # last
            
            tracked_cont, tracked_img = track_complete.track_complete(cont13, cont23_img)
            tracked_img = rect_detect.rect_detect(tracked_cont,tracked_img.shape)
            tracked_cont, _ = cv2.findContours(tracked_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            per_dir.per_dir(cont_base_img, cont_base, tracked_img, tracked_cont, tracked_img.shape)

            second = third              #for the following tracks, update second image


        if pressed == ord('b'):
            ret, base = vid.read()
            base = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
            base = rescaleFrame(base, 0.6)
            #first = perspective.perspective(first)

            # Display the resulting frame
            cv2.imshow('Base', base)
            cv2.imwrite('VideoCapture\TestImages\Base.jpeg', base)

            cont_base, cont_base_img = img_compare.img_compare(first, base)

        # to quit, use key 'q'
        elif pressed == ord('q'): 
            break

        # to destroy windows, use key 'd'
        elif pressed == ord('d'):
            cv2.destroyAllWindows()

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
