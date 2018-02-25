# coding: utf-8

import numpy as np
import cv2

# OpenCVで画像読み込み
img = cv2.imread("sample.jpg", 0)
# 画像出力
cv2.imshow("sample", img)
cv2.waitKey(0)
cv2.destroyAllWindows()