# coding: utf-8

import numpy as np
import cv2


img = cv2.imread("./sample.jpg")

# ノイズ除去
my_img = cv2.fastNlMeansDenoisingColored(img)

cv2.imshow("sample", my_img)
cv2.imwrite("removed_noize.jpg", my_img)

img = cv2.imread('./sample2.jpg')
my_img2 = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imwrite("removed_noize2.jpg",my_img2)
cv2.imshow("sample2", my_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()