# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("./sample.jpg")

# 第二引数を0にするとチャンネル数1画像を生成
mask = cv2.imread("./mask.png", 0)

# 元の画像と同じサイズ
mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

# 第三引数でマスク用の画像を選ぶ
my_img = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("sample", my_img)
cv2.imwrite("masked.jpg", my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()