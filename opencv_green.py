#importing libraries
import cv2
import numpy as np

#set our upper and lower bounds for Hue, Saturation, and Value
lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])

#initialize camera object
cam= cv2.VideoCapture(0)

#uses kernal to prevent holes and dots 
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))


#creates a font
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)

#begin the loop
while True:
	#read frame from the camera
	ret, img=cam.read()

	#resize it
	img=cv2.resize(img,(340,220))

	#convert to hsv
	imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#create the filter which creates the mask for green
	mask=cv2.inRange(imgHSV,lowerBound,upperBound)
	
	#morphology stuff
	maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    	maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
	
	#the 'final form' 
	maskFinal=maskClose
    	conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(img,conts,-1,(255,0,0),3)
	
	#loop through all of the contours in conts, put a rectangle over and mark for tracking
	for i in range(len(conts)):
        	x,y,w,h=cv2.boundingRect(conts[i])
        	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
        	cv2.cv.PutText(cv2.cv.fromarray(img), str(i+1),(x,y+h),font,(0,255,255))

	#actually do the thing
	cv2.imshow("maskClose",maskClose)
    	cv2.imshow("maskOpen",maskOpen)
    	cv2.imshow("mask",mask)
    	cv2.imshow("cam",img)
cv2.waitKey(10)
