import cv2 as cv

# rescales images for visualization purposes
# for display
def rescaleFrame(frame, scale = 0.75):
    #images,videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)