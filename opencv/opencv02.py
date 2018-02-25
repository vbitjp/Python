# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("sample.jpg")
# 入力画像をネガポジ反転
img = cv2.bitwise_not(img)
'''
時間計算量がO(n^3)に増えることを除けば、for文で書き換えた場合以下のとおり
for i in range(len(img)):
    for j in range(len(img[i])):
        for k in range(len(img[i][j])):
            img[i][j][k] = 255 - img[i][j][k]
'''
# ファイル保存
cv2.imwrite("nega_posi_conversion.jpg", img)

cv2.imshow("sample", img)
cv2.waitKey(0)
cv2.destroyAllWindows()