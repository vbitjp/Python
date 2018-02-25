# coding: utf-8

import numpy as np
import cv2

# 画像サイズ
img_size = (512, 512)

# サイズが512 × 512の緑色画像
my_img = np.array([[[0, 255, 0] for _ in range(img_size[1])] for _ in range(img_size[0])], dtype="uint8")
# 赤の場合はnp.array([[[0, 0, 255] for _ in range(img_size[1])] for _ in range(img_size[0])], dtype="uint8")
'''
「for _ in range」の _ は、for文で繰り返す際に、_ にあたる変数をfor文の中で使わない場合に使用する
1つめのforで横に512枚の画像、2つめのforでさらに縦に512枚の画像を作成する
'''
cv2.imshow("sample", my_img)

cv2.imwrite("my_green_img.jpg", my_img)