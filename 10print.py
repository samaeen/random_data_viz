import random
import cv2
import numpy as np

height=400
width=600

x=0
y=0
spacing=10

count=0

img = np.zeros((height,width,3), np.uint8)


while count<4000:
	randNum=random.random()
	if randNum>.5:
		cv2.line(img,(x,y),(x+spacing,y+spacing),(255,255,255),2)
	if randNum<.5:
		cv2.line(img,(x,y+spacing),(x+spacing,y),(255,255,255),2)
	x=x+spacing

	if x>width:
		x=0
		y=y+spacing
	count=count+1


cv2.imwrite("10print.jpg",img)
cv2.imshow('10print',img)
cv2.waitKey(0)
