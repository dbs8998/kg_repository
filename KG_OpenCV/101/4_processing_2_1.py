# 비디오 캡쳐 + 이미지 회색 변환

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
    ret, frame = cap.read()

    if ret:
        # BGR -> GRAY
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    cv2.imshow("GRAY", img_gray)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()