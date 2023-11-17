
import numpy as np
import cv2
import math
#import VideoCapture.perspective as perspective

def rescaleFrame(frame, scale = 0.75):
    #images,videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)


#img = cv2.imread("D:\Desktop\GITHUB\Engineering-Design\\03-Software\\3-coverage control\line_detect\Rectangles.jpg",cv2.IMREAD_COLOR)
#img = cv2.imread("D:\Desktop\GITHUB\Engineering-Design\\03-Software\\3-coverage control\VideoCapture\second.jpeg",cv2.IMREAD_COLOR)
#img = cv2.imread("D:\Desktop\GITHUB\Engineering-Design\\03-Software\\3-coverage control\image comparison\WhatsApp Image 2022-12-16 at 16.46.15.jpeg",cv2.IMREAD_COLOR)
img = cv2.imread("D:\Desktop\camera-samples\sample_120_2.png",cv2.IMREAD_COLOR)

img = rescaleFrame(img, 0.6)

#p_img = perspective.perspective(img)
#cv2.imshow("percpective",p_img)

gray_org = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.bilateralFilter(gray_org, 0, 20, cv2.BORDER_DEFAULT)
gray = cv2.GaussianBlur(gray_org,(5,5),0)

edges = cv2.Canny(gray, 75, 150)

#lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=100, minLineLength=50)
#lines = cv2.HoughLinesP(edges, 1, np.pi/120, 50, maxLineGap=120, minLineLength=150)

print(lines)
print ("length: ", len(lines))
numOfHoriz = 0
tente = 0
tenteY = 0           

for line in lines:
    x1, y1, x2, y2 = line[0]

    # find angle of the lines
    angle = np.arctan(abs(y2-y1) / abs(x2 - x1))
    
    # find horizontal lines
    if (angle < 15*(math.pi/360)) :

        # find length of the lines
        length = math.sqrt((y2-y1)**2 + (x2 - x1)**2)

        if (length > 120):      # may be deleted
            # limit the length of the horizontal lines
            #cv2.line(img, (x1,y1), (x2, y2), (0, 0, 255), 2)        # red
            numOfHoriz = numOfHoriz + 1
            print("Horizontal line",line, "length: ", length)
            if y1 > tenteY:
                # find the horizontal line at the belowest
                tenteY = y1
                tente = line[0]

    #else:
        # non-horizontal lines
        # cv2.line(img, (x1,y1), (x2, y2), (0, 255, 0), 2)

# founded line that is the one side of the canopy
x1, y1, x2, y2 = tente
cv2.line(img, (x1,y1), (x2, y2), (255, 0, 0), 2)        # blue
print("Blue Horizontal line",tente)

for line in lines:
    x1, y1, x2, y2 = line[0]

    if y1 > tenteY or y2 > tenteY:
        cv2.line(img, (x1,y1), (x2, y2), (0, 255, 0), 2)        # green


cv2.imshow("edges",edges)
cv2.imshow("Image", img)

print ("Number of Horizontal lines: ", numOfHoriz)

cv2.waitKey(0)
cv2.destroyAllWindows()