import cv2
import datetime
# pip install pillow
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 객체 생성
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 폰트 불러오기
font = ImageFont.truetype(r"C:\Users\AI06\Documents\_Pr_1\Python\OpenCV\fonts\SCDream6.otf", 15)

# 실행
while True:
    ret, frame = cap.read()

    # 현재 시각 -> 문자열
    t_now = datetime.datetime.now()
    t_now_str = t_now.strftime('%Y/%m/%d %H:%M:%S')

    # 글자가 잘 보이도록 배경 설정
    cv2.rectangle(img=frame, pt1=(10, 10), pt2=(350, 35), color=(0,0,0), thickness=-1)

    # 영상 이미지에 요소(글자)를 넣기
    # Numpy -> Pillow 배열로 변환
    frame = Image.fromarray(frame)
    # 이미지 추가
    draw = ImageDraw.Draw(frame) 
    draw.text(xy=(10, 15), text="내가 너를 봤다!"+t_now_str, font=font, fill=(255, 255, 255))

    # 다시 Numpy 배열 이미지로 전환함.
    frame = np.array(frame)

    cv2.imshow("CCTV", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()