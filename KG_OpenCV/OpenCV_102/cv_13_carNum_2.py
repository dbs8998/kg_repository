# https://www.youtube.com/watch?v=PpTl7xxGXh4

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract   #pip install pytesseract

plt.style.use("dark_background")

## 1. 이미지 읽기
img_src = cv2.imread('images/1.jpg')

height, width, channel = img_src.shape

plt.figure(figsize=(12, 10))
plt.imshow(img_src, cmap='gray')  # 소스 이미지 표시를 위해 여러 컬러맵(cmap) 중 gray 맵을 사용함.

## 2. Grayscale로 변환
gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(12, 10))
plt.imshow(gray, cmap='gray')  # gray 이미지 표시를 위해 여러 컬러맵(cmap) 중 gray 맵을 사용함.

## 3. [옵션] Contrast 극대화
structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
imgTopHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, structuringElement)
imgBlackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, structuringElement)

imgGrayscalePlusTopHat = cv2.add(gray, imgTopHat)
gray = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)

plt.figure(figsize=(12, 10))
plt.imshow(gray, cmap='gray')
plt.show()

## 4. Adaptive Thresholding
# 가우시안 블러를 안 하고 threshold만 한 경우
img_thresh= cv2.adaptiveThreshold(
    gray,   # gray 스케일 이미지
    maxValue=255.0,  # 임계값 이상일 때 적용할 최대한계값(여기서는 흰색255)
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, #적응적 임계값 처리방법 = 가우시안 가중치 평균 적용
    thresholdType=cv2.THRESH_BINARY_INV, # 임계값 유형 = 이진화된 반전값
    blockSize=19,     # 이웃 픽셀의 크기(픽셀 영역)
    C=9     # (가중)평균에서 뺄 값
)

# blur와 threshold를 한 경우 (gray scale, 커널 크기 5x5, X방향 가우시안 커널 표준 편차(0 이면 커널을 따라 자동 계산))
img_blurred = cv2.GaussianBlur(gray, ksize=(5, 5), sigmaX=0)
img_blur_thresh = cv2.adaptiveThreshold(
    img_blurred,
    maxValue=255.0,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY_INV,
    blockSize=19,
    C=9
)

plt.figure(figsize=(12, 10))
plt.subplot(1, 2, 1)
plt.title('Threshold only')
plt.imshow(img_thresh, cmap='gray')
plt.figure(figsize=(12, 10))
plt.subplot(1, 2, 2)
plt.title('Blur and Threshold')
plt.imshow(img_blur_thresh, cmap='gray')

plate_cx, plate_cy = 508.75, 300.5  # 번호판 중앙점 x, y좌표
width, height = 940, 626
plate_width, plate_height = 188.5, 49
angle = 11.9565

rotation_matrix = cv2.getRotationMatrix2D(center=(plate_cx, plate_cy), angle=angle, scale=1.0)
img_rotated = cv2.warpAffine(img_thresh, M=rotation_matrix, dsize=(width, height))

plt.figure(figsize=(12, 10))
plt.subplot(1, 2, 1)
plt.title("Threshold")
plt.imshow(img_blur_thresh, cmap='gray')
plt.figure(figsize=(12, 10))
plt.subplot(1, 2, 2)
plt.title('Rotate')
plt.imshow(img_rotated, cmap='gray')

img_cropped = cv2.getRectSubPix(
    img_rotated,
    patchSize=(int(plate_width), int(plate_height)),
    center=(int(plate_cx), int(plate_cy))
)

plt.figure(figsize=(12, 10))
plt.imshow(img_cropped, cmap='gray')
# plt.show() # 이미지를 화면에 표시

## 5. Find Contours
# 5.1 Contour 찾기
contours, _ = cv2.findContours(img_thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

temp_result = np.zeros((height, width, channel), dtype=np.uint8)

# 5.2 Contour 그리기 (-1: 모든 칸투어 그리기)
cv2.drawContours(temp_result, contours=contours, contourIdx=-1, color=(255, 255, 255))

plt.figure(figsize=(12, 10))
plt.imshow(temp_result)

# 6. Prepare Data
temp_result = np.zeros((height, width, channel), dtype=np.uint8) #0으로 채우기

contours_dict = [] # 컨투어별 바운딩 박스의 x, y, w, h 넣을 배열

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(temp_result, pt1=(x, y), pt2=(x+w, y+h), color=(255, 255, 255), thickness=2)

    # insert to dict
    contours_dict.append({
        'contour': contour,
        'x': x,
        'y': y,
        'w': w,
        'h': h,
        'cx': x + (w / 2),
        'cy': y + (h / 2)
    })
    
    plt.figure(figsize=(12, 10))
    plt.imshow(temp_result, cmap='gray')
    plt.show() 

# 7. Bounding box의 사이즈/비율로 읽을 후보 선정 (번호판 글자는 일정 규격)
MIN_AREA = 80
MIN_WIDTH, MIN_HEIGHT = 2, 8
MIN_RATIO, MAX_RATIO = 0.25, 1.0

possible_contours = []

cnt = 0
for d in contours_dict:
    area = d['w'] * d['h']
    ratio = d['w'] / d['h']
    
    if area > MIN_AREA \
    and d['w'] > MIN_WIDTH and d['h'] > MIN_HEIGHT \
    and MIN_RATIO < ratio < MAX_RATIO:
        d['idx'] = cnt
        cnt += 1
        possible_contours.append(d)

# visualize possible contours
temp_result = np.zeros((height, width, channel), dtype=np.uint8)

for d in possible_contours:
    # cv2.drawContours(temp_result, d['contour'], -1, (255, 255, 255))
    cv2.rectangle(temp_result, pt1=(d['x'], d['y']), pt2=(d['x']+d['w'], d['y']+d['h']), color=(255, 255, 255), thickness=2)

plt.figure(figsize=(12, 10))
plt.imshow(temp_result, cmap='gray')
plt.show()

###############
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

def process_image(image_path, show_steps=False):
    # 이미지 파일을 읽어옵니다.
    image = cv2.imread(image_path)
    
    # 그레이스케일로 변환합니다.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 가우시안 블러를 적용하여 이미지를 부드럽게 만듭니다.
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 케니 엣지 검출을 사용하여 이미지에서 엣지를 찾습니다.
    edges = cv2.Canny(blurred, 50, 150)
    
    # 엣지 이미지에서 컨투어를 찾습니다.
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 컨투어를 따라 이미지에 사각형을 그립니다.
    image_with_rectangles = image.copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image_with_rectangles, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # 처리된 이미지를 화면에 표시합니다.
    if show_steps:
        plt.imshow(image_with_rectangles)
        plt.title("Image with Rectangles")
        plt.show()
    
    # 이미지에서 텍스트를 추출합니다.
    extracted_text = pytesseract.image_to_string(image, lang='eng')
    
    return extracted_text

# 이미지 파일 경로
image_path = 'example_image.jpg'

# 이미지 처리 함수 호출
extracted_text = process_image(image_path, show_steps=True)

# 추출된 텍스트 출력
print("Extracted Text:")
print(extracted_text)
'''