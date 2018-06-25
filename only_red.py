#! /usr/bin/pythin3

import os
import cv2

#reading the image
img=cv2.imread('flower.jpg',1)
#storing only the red part using inRange method
onlyred=cv2.inRange(img,(0,0,0),(40,40,255))
cv2.imshow('red_img',onlyred)
cv2.imwrite('red_img.jpg',onlyred)

#now seeing only red part in the video
cap=cv2.VideoCapture(0)

while cap.isOpened() :
  status,frame=cap.read()
  onlyred1=cv2.inRange(frame,(0,0,0),(50,60,255))
  cv2.imshow("red_video",onlyred1)
  if cv2.waitKey(1) & 0xFF==ord('q') :
    break
cv2.destroyAllWindows()
cv2.release()
