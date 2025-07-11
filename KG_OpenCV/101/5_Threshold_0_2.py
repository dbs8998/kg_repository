# adaptiveThreshold(): 적응형 임계값

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('101/Images/person_2.jpg', cv2.IMREAD_GRAYSCALE)

adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

plt.imshow(adapt, cmap='gray')
plt.title("Adaptive Thresh")
plt.show()