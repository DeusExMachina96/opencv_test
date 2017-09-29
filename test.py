import cv2

print(cv2.__version__)

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ans = False
    while ans == False:
        ret, frame = cap.read()
        ans = ret

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(ret)
    # frame = np.array((np.array(frame)*-1), dtype='uint8')
    # frame = cv2.flip(frame, flipCode=1)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1)== ord('q'):
        break
    # print()
    # break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
