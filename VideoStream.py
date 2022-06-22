#from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import cv2
import os
import time
#import imutils

vs = cv2.VideoCapture('sample.mp4')
cropping = False

x_start, y_start, x_end, y_end = 0, 0, 0, 0
a=0
l=1
flag = True

def rectangleDraw():
    cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
    cv2.imshow("image", image)

def mouse_crop(event, x, y, flags, param):

    global x_start, y_start, x_end, y_end,a , cropping, oriImage, ret, flag, l, recPoint, cache, image


    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
        cv2.imshow("image", image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        ret = False
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
            recPoint = [(x_start, y_start), (x_end, y_end)]

    elif event == cv2.EVENT_LBUTTONUP:
        x_end, y_end = x, y
        cropping = False 
        refPoint = [(x_start, y_start), (x_end, y_end)]
        f = len(recPoint)
        f=f-1
        cache = image.copy()
        cv2.rectangle(cache, (recPoint[0][0], recPoint[0][1]), (recPoint[f][0], recPoint[f][1]), (255, 0, 0), 2)
        cv2.imshow("image", cache)

        if len(refPoint) == 2: 
            roi = oriImage[refPoint[0][1]+2:refPoint[1][1]-2, refPoint[0][0]+2:refPoint[1][0]-2]
            a=a+1

            cv2.imwrite('img%.0f.bmp'%a,roi)

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)

while 1:
        ret,oriImage = vs.read()
        image=oriImage
        i=image.copy()

        if ret==True:
            if not cropping:
                cv2.imshow("image", image)

            elif cropping:
                rectangleDraw()

            k = cv2.waitKey(1) & 0xFF
            if k == ord("q"):
                break

        if ret == False:
                cv2.waitKey()
                rectangleDraw()
                ret = True

vs.release()
cv2.destroyAllWindows()
