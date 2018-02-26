# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("./sample.jpg")

# 二値化
# 第一引数=処理する画像, 第二引数=しきい値, 第三引数=最大値(maxvalueとする)
# 第四引数=THRESH_BINARY, THRESH_BINARY_INV, THRESH_TOZERO, THRESH_TRUNC, THRESH_TOZERO_INVのいずれか
# THRESH_BINARY:しきい値より大きい値はmaxvalueに、そうでないものは0になる、THRESH_BINARY_INVはその逆
# THRESH_TRUNC:しきい値より大きい値はしきい値に、そうでないものはそのまま
# THRESH_TOZERO:しきい値より大きい値はそのまま、小さい値は0になる、THRESH_TOZERO_INVはその逆
# しきい値はretvalで受け取る
retval, my_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("sample", my_img)
cv2.imwrite("tobinary.jpg", my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()