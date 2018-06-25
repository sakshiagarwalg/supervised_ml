#!/usr/bin/python3
import numpy
import os
import cv2
#loading the image
img=cv2.imread('cat.jpg')
img1=cv2.imread('cat.jpg',0)
#printing the width and height
print(img.shape)
#showing the image
cv2.imshow('cat',img)
cv2.imshow('catbw',img1)
#to activate the image window holder
cv2.waitKey(0)
cv2.destroyAllWindows()
