import cv2
import matplotlib.pyplot as plt

img_color = cv2.imread('101/Images/person_2.jpg', cv2.IMREAD_COLOR)

# BGR -> RGB
b, g, r = cv2.split(img_color)    # 파랑 사진
img_color2 = cv2.merge([r, g, b]) # 정상 사진

plt.imshow(img_color2)
plt.xticks([])
plt.yticks([])
plt.show()