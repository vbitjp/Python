# coding: utf-8

import numpy as np
import cv2

img = cv2.imread("./sample.jpg")

mask = cv2.imread("./mask.png", 0)
mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

# sample.jpgからmask.pngの黒塗り箇所を取り出す
retval, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV)

my_img = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("sample", my_img)
cv2.imwrite("masked2.jpg", my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()