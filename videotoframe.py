import numpy as np
import cv2
import sys

f1 = sys.argv[1] #input file path .//Downloads/LV2.mp4
f2 = sys.argv[2] #output folder path in this format ./LavanyaTripaty/lavanyatripati1-
cap = cv2.VideoCapture(f1)
count = 0
while(count<9000 && cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite(f2+str(count)+'.png',frame)
    count = count + 1
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('video live stream',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
