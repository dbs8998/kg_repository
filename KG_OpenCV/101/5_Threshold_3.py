# https://opencv-python.readthedocs.io/en/latest/doc/09.imageThresholding/imageThresholding.html
# Adaptive Threshold 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('101/Images/person_1.png', 0)
# img = cv2.medianBlur(img, 5)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)
thresh3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2)

titles = ['Source', 'Global', 'Mean', 'Gaussian']
images = [img, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()