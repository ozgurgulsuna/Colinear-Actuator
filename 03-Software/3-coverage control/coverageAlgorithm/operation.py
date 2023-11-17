# this is the main code for coverage detection algorithm

# import opencv library
import cv2 as cv

# main functions
import per_dir_2
import img_compare
import perspective_2
import rect_detect

# not essential visualization functions
import visualization as vs

# necessary to add delays to the system
import time

# define a video capture object
vid = cv.VideoCapture(0)                                                # 0 : webcam, to find other cameras, change the number

# background image is added to the system, image is determined in advance during calibration
background_path = "3-coverage control/coverageAlgorithm/Background.jpeg"
background_image = cv.imread(background_path)
background_image = cv.cvtColor(background_image, cv.COLOR_BGR2GRAY)

# repeat the same operation steps until the operation is terminated
while(1):
    # to see the video, not essential for operation
    # Capture the video frame by frame
    ret, frame = vid.read()
    # Display the resulting frame
    cv.imshow('Live Video', frame)
    
    # determine pressed key, used for test purposes
    pressed = cv.waitKey(1) & 0xFF

    # to stop video stream, press "q"
    if (pressed == ord('q')):
        cv.destroyAllWindows()
        break
    # background image for faster test, only test purposes
    if (pressed == ord('b')):
        ret, background_image = vid.read()
        background_image = cv.cvtColor(background_image, cv.COLOR_BGR2GRAY)
        cv.imshow('Base', background_image)
        cv.imwrite(background_path, background_image)
    # capture an image to process
    if (pressed == ord('c')):
        start = time.time()

        # Capture a frame
        ret, image = vid.read()
        # convert image to gray scale
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv.imshow('Image to process', image)

        # compare image with background image
        cont, cont_img = img_compare.img_compare(background_image, image)
        cv.imshow('Compared Image', cont_img)

        # perspective correction
        perspective_img = perspective_2.perspective_2(cont_img)
        cv.imshow('Perspective Corrected Image', perspective_img)
        #perspective_img = cv.cvtColor(perspective_img, cv.COLOR_BGR2GRAY)
        _,thresh=cv.threshold(perspective_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        pers_cont, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Largest interior rectange detection
        rect_img, rect_points = rect_detect.rect_detect([pers_cont],perspective_img.shape)
        cv.imshow('Detected Largest Interior Rectangle', rect_img)

        per_dir_2.per_dir(shape = rect_img.shape, rect_points=rect_points)

        end = time.time()
        print("operation time:", (end - start), "   "   "seconds")

    """
    # Delay for proper operation, may not be used at all
    time.sleep(0.5)         # wait in seconds
    """



# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()