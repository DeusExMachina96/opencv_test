
import cv2

print(cv2.__version__)
#prints out the version number of the cv2 package

cap = cv2.VideoCapture(0)
#opens a video capture object, uses the webcam on your computer

while True:
#this is just a while loop, this is where the magic happens

	# Capture frame-by-frame
	ans = False
	#assume that it didn't capture the right image, and keep checking until you get something
	while ans == False:
		ret, frame = cap.read()
		#the cap.read returns a boolean of success and the actual frame
		ans = ret
		#return the answer
	
# Our operations on the frame come here
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# print(ret)
# frame = np.array((np.array(frame)*-1), dtype='uint8')
    
	#frame = cv2.flip(frame, flipCode=1)
	#this mirrors, or flips the frame along the y axis, put zero to put it upsidedown

# Display the resulting frame
	
	cv2.imshow('frame', frame)
	#takes a cv2 image and displays it, the string is the name of the popup window
	if cv2.waitKey(1)== ord('q'):
		break
	#waitKey pauses and gives you time to draw and update the image, always need it 
	#pauses and checks if you've pressed 'q' to quit
	#print()
	#break

#when everything down, release the capture
cap.release()
#shuts off the webcam
cv2.destroyAllWindows()
#destroys the popup window, closes it essentially