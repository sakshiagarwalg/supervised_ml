#! /usr/bin/python3

import os
import cv2
import random

cap=cv2.VideoCapture(0)

while cap.isOpened() :
  print("camera is ready") 
  # reading the captured image and storing its status and frame
  status,frame=cap.read()	
  # converting the image into black and white      
  bw_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #drawing the line on both
  cv2.line(frame,(10,10),(40,40),(190,67,250),3)
  cv2.line(bw_img,(10,10),(40,40),(190,67,250),3)
  # drawing the rectangle on both
  cv2.rectangle(frame,(400,200),(500,300),(190,67,250),10)
  cv2.rectangle(bw_img,(400,200),(500,300),(190,67,250),10)
  # drawing the circle on both
  cv2.circle(frame,(200,300),50,(190,67,250),10)
  cv2.circle(bw_img,(200,300),50,(190,67,250),10)
  # writing text
  # defining font
  #font=cv2.FONT_HERSHEY_SIMPLEX
  #cv2.putText(frame,"sakshi photo", (100,100),font,3,(255,0,0),cv2.line_AA)
  # displaying the image
  cv2.imshow("camera",frame)
  cv2.imshow("CAMERA 1",bw_img)
'''
  # storing all the captured frames
  x=random.random()
  y=str(x)[2:6]
  cv2.imwrite('adhoc'+y+'.jpg',frame)
  # holding the frame window
'''
  if cv2.waitKey(1) & 0xFF==ord('q') :
    break

# releasing the windows
cv2.destroyAllWindows()
cap.release()
