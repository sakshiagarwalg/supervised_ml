#! /usr/bin/python3

import cv2
import numpy
cap=cv2.VideoCapture(0)
face =cv2.CascadeClassifier('face_data.xml')

while cap.isOpened() :
	status,frame=cap.read()
	#grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face.detectMultiScale(frame,1.15,5)
	for (x,y,w,h) in faces :
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
		#roi_gray=frame[y:y+h,x:x+w]
		roi_color=frame[y:y+h,x:x+w]
		#displaying the frame
		cv2.imshow("original",frame)
		cv2.imshow("face_img",roi_color)
		#print(grayimg)
	if cv2.waitKey(1) & 0xFF==ord('q') :
		#cv2.imwrite("img.jpeg",frame)
		break
cap.release()
cv2.destroyAllWindows()

