#! /usr/bin/python3

import os
import cv2

cap=cv2.VideoCapture(0)

if cap.isOpened() :
   print("camera is ready")
   # reading the captured image and storing its status and frame
   status,frame=cap.read()
   # converting the image into black and white
   bw_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # displaying the image
   cv2.imshow("CAMERA 1",bw_img)
   # holding the frame window
   cv2.waitKey(0)
# releasing the windows
cv2.destroyAllWindows()
cap.release()
