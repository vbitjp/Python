# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("./sample.jpg")

# warpAffine()を用いるのに必要な行列
mat = cv2.getRotationMatrix2D(tuple(np.array(img.shape[:2]) / 2), 180, 1.0)
# 第一引数=回転の中心(今回は画像の中心)、第二引数は回転角度(今回は180度)、第三引数は倍率

# アフィン変換
my_img = cv2.warpAffine(img, mat, img.shape[:2])
# 第一引数=変換したい画像、第二引数=上で生成した行列(mat)、第三引数=サイズ

cv2.imshow("sample", my_img)
cv2.imwrite("affin_180deg_rotated.jpg", my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()