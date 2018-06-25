#!/usr/bin/python3
import numpy
import cv2
import os
# all functions of  cv2  that is opencv model  
# reading image
# image name , image features  
# we can write    cv2.IMREAD_COLOR instead of 1 
# we can write    cv2.IMREAD_BGR2GRAY instead of 0
# we can write    cv2.IMREAD_UNCHANGE_COLOR instead of -1

img=cv2.imread("cat.jpg",1)
img1=cv2.imread("cat.jpg",0)
img2=cv2.imread("cat.jpg",-1)

#  checking rows and cols 
#print(img.shape)
#print(img1.shape)

# to show original data of image  
#print(img)

# to show images 
cv2.imshow("meow",img)
cv2.imshow("sun",img1)
cv2.imshow("rabbit",img2)

# save the images image
cv2.imwrite("bwsun.jpg",img2)
#cv2.imwrite("rabbi.jpg",img3)

#  to hold  upper window  
cv2.waitKey(0)
cv2.destroyAllWindows()
