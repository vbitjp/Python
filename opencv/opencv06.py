# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("./sample.jpg")

# 第2引数が0のときx軸中心に、正のときy軸中心に、負のとき両方の軸を中心に反転
my_img = cv2.flip(img, 0)

cv2.imshow("sample", my_img)
cv2.imwrite("affin_180deg_rotated2.jpg", my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()