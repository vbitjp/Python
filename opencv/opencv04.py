# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("./sample.jpg")

size = img.shape
# サイズの商を取ればn等分できる
my_img = img[: size[0] // 3, : size[1] // 3]

# 今回はもとの倍率を保ったまま幅と高さをそれぞれ1/3倍する。
# 新たにサイズを指定する際、(幅、高さ)の順になることに注意
my_img = cv2.resize(my_img, (my_img.shape[1], my_img.shape[0]))
# 2/3倍の場合は cv2.resize(my_img, (my_img.shape[1] * 2, my_img.shape[0] * 2)) となる
cv2.imshow("trim", my_img)
cv2.imwrite("trim.jpg", my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()