import cv2

img_path = "C:/Users/AI06/Documents/_Pr_1/Python/OpenCV/images/ball_1.png"
img_color = cv2.imread(img_path)
cv2.imshow("Color_Window", img_color)
cv2.imwrite(img_path, img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Window", img_gray)
cv2.waitKey(0)
# cv2.imwrite(img_path, img_gray)