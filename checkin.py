import numpy as np
import cv2

cap = cv2.VideoCapture('Check-in.avi')

while(cap.isOpened()):
    ret, img = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
