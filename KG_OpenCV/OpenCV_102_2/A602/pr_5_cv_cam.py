# 저장한 동영상 읽어와서 흑백 동영상과 함께 재생하기

import cv2

cap = cv2.VideoCapture("myVideo_1.avi")

fourcc = cv2.VideoWriter_fourcc(*"XVID")

while(True):
    ret, img_color = cap.read()

    if ret == False:
        break

    # 칼라로 읽어온 동영상을 흑백으로 바꿈. 코덱이 없어서 동영상을 못읽으면 컨버트도 안 되고 이후 작업의 결과가 안 나옴. 이 경우 팟플레이어 설치 후 진행하면 됨.
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Color_copy", img_color)
    cv2.imshow("Gray_copy", img_gray)

    # 녹화를 30프레임/초로 했음. -> 대기 시간을 30으로 설정해야 정상속도로 재생됨. 비교를 위해 waitKey(1)로 해보면 앎. 
    if cv2.waitKey(30)&0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()