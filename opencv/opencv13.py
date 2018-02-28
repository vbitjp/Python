# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("./sample.jpg")

# フィルタの定義

filt = np.array([[0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]], np.uint8)
'''
filt = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]], np.uint8)
'''
# 膨張(という名のノイズ除去)
# see also http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

my_img = cv2.erode(img, filt)

cv2.imshow("sample", my_img)
cv2.imwrite("erode.jpg", my_img)
# 比較のため元の写真を表示
cv2.imshow("original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()