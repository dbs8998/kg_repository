import cv2
import numpy as np

img = cv2.imread('color_test.jpg')
img = cv2.resize(img, (680,480))

#트랙바 세팅
cv2.namedWindow('track')

def do_pass(x):
    pass

cv2.createTrackbar('h_min', 'track', 0,180,do_pass)
cv2.createTrackbar('s_min', 'track', 0,255,do_pass)
cv2.createTrackbar('v_min', 'track', 0,255,do_pass)

cv2.createTrackbar('h_max', 'track', 180,180,do_pass)
cv2.createTrackbar('s_max', 'track', 255,255,do_pass)
cv2.createTrackbar('v_max', 'track', 255,255,do_pass)



while True:
    try:
        #hsv 생성
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        #트랙바 데이터 가져오기
        h_min = cv2.getTrackbarPos('h_min', 'track')
        s_min = cv2.getTrackbarPos('s_min', 'track')
        v_min = cv2.getTrackbarPos('v_min', 'track')
        h_max = cv2.getTrackbarPos('h_max', 'track')
        s_max = cv2.getTrackbarPos('s_max', 'track')
        v_max = cv2.getTrackbarPos('v_max', 'track')

        low = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        output = img.copy()

        #색상범위로 마스크 생성하여 이미지에 해당하는 색상만 남도록 필터링

        #mask 생성
        mask = cv2.inRange(hsv, low, upper)

        result = cv2.bitwise_and(output, output, mask=mask)


        #윤곽선 검출, 사각형으로 결과 표시
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100: #너무 작은 노이즈는 제외
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(result, (x,y), (x+w, y+h), (0,255,0),2)

        

        cv2.imshow('mask',mask)
        cv2.imshow('result',result)


        if cv2.waitKey(1) & 0xFF == 27:
            break
    except Exception as e:
        print(e)
        break

cv2.destroyAllWindows()

