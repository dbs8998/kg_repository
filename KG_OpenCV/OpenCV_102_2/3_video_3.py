# 영상 저장

import cv2

vCap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter('Capture/capture1.avi', fourcc, 25.0, (640,480))

while(vCap.isOpened()):
    ret, frame = vCap.read()
    
    if ret:
        # 이미지 반전, 0: 상하, 1: 좌우
        frame = cv2.flip(frame, 1)
        writer.write(frame)

        cv2.imshow("Capture", frame)

        if cv2.waitKey(1) & 0xff == ord('q'): # 원문 오류 수정함
            break
    else:
        break

vCap.release()
writer.release()
cv2.destroyAllWindows()