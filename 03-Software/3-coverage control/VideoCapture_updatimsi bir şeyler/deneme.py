import cv2
import background
import img_compare
import rect_detect

img1=cv2.imread('Shadow2.jpeg', cv2.IMREAD_COLOR)
img2=cv2.imread('Third.jpeg', cv2.IMREAD_COLOR)
img1=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cont, cont_img = img_compare.img_compare(img1, img2)
cv2.imshow("hey",rect_detect.rect_detect(cont,cont_img.shape))
cv2.waitKey(0)