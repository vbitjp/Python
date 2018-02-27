# coding: utf-8

import numpy as np
import cv2


img = cv2.imread("./sample.jpg")

# ノイズ除去
my_img = cv2.fastNlMeansDenoisingColored(img)

cv2.imshow("sample", my_img)
cv2.imwrite("removed_noize.jpg", my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()