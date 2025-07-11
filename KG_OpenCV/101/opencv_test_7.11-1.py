# ✅ 1️⃣ 하급 (쉬움 ⭐️) 문제 3개
# ✅ 문제 1 (하급 ⭐️)
# [이미지 읽어서 출력하기]

# ✅ 조건:

# OpenCV로 로컬 이미지 파일을 읽어

# 새 창에 출력

# ✅ 목표 함수/메서드:

# cv2.imread(), cv2.imshow(), cv2.waitKey()

import cv2

img_path = 'Images/person_1.png'

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
print(img.shape) # 리턴된 img 행렬: (246, 205, 3)

img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

while True:

    #이미지 출력
    #imshow(title,val) - title : 오픈되는 창의 제목, val - 이미지 값
    cv2.imshow('gray',img_gray)
    # cv2.waitKey(0)
    #이미지 유지, 
    if cv2.waitKey(1) & 0xff == 27:
        cv2.destroyAllWindows()
        break



