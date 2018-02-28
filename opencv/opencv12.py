# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("./sample.jpg")

# 第一引数=元の画像, 第二引数=n✕nのnの値(nは奇数), 第三引数はx軸方向の偏差(通常は0)
my_img = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("sample", my_img)
cv2.imwrite("blured.jpg", my_img)

img = cv2.imread("./sample2.jpg")

my_img = cv2.GaussianBlur(img, (111, 111), 0)
cv2.imshow("sample2", my_img)
cv2.imwrite("blured2.jpg", my_img)

cv2.waitKey(0)
cv2.destroyAllWindows()