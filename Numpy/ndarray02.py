#!/usr/bin/env python
# coding: utf-8
'''
Numpyの高速な処理の体験
自機Macでの実行結果
Python組み込みモジュールのみでの実行時間：1.26[sec]
Numpyを使った場合の実行時間：0.00[sec]
'''
# 必要なライブラリをimport
import numpy as np
import time
from numpy.random import rand

# 行、列の大きさ
N = 100

# 行列の初期化
matA = np.array(rand(N, N))
matB = np.array(rand(N, N))
matC = np.array([[0] * N for _ in range(N)])

# Pythonのリストを使って計算

# 開始時間の取得
start = time.time()

# for文を使って行列の掛け算を実行。計算量はO(N^3)
for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] = matA[i][k] * matB[k][j]

print("Python組み込みモジュールのみでの実行時間：%.2f[sec]" % float(time.time() - start))

# Numpyを使って計算

# 開始時間の取得
start = time.time()

# Numpyを使って行列の掛け算を実行
matC = np.dot(matA, matB)

# 少数第2位の桁で打ち切っているのでNumpyは0.00[sec]と表示されます。
print("Numpyを使った場合の実行時間：%.2f[sec]" % float(time.time() - start))


'''
Numpyの行列は標準のリストと挙動が異なる
'''

# Pythonのリストでスライスを用いた場合の挙動
arr_List = [x for x in range(10)]
print(arr_List)

arr_List_copy = arr_List[:]
arr_List_copy[0] = 100

# リストのスライスではコピーが作られる。arr_Listにはarr_Listの変更が反映されない。
print(arr_List)

# Numpyのndarrayでスライスを用いた場合での挙動
arr_Numpy = np.arange(10)
print(arr_Numpy)

arr_Numpy_view = arr_Numpy[:]
arr_Numpy_view[0] = 100

# Numpyのスライスではビュー(データが格納されている場所の情報)が代入される。
# 奇妙なことに、arr_Numpy_viewの変更がarr_Numpyに反映される。
print(arr_Numpy)

# Numpyのndarrayでcopy()を用いた場合での挙動
arr_Numpy = np.arange(10)
print(arr_Numpy)

arr_Numpy_copy = arr_Numpy[:].copy()
arr_Numpy_copy[0] = 100

# copy()を用いた場合は、arr_Numpy_copyはarr_Numpyに影響を与えない。
print(arr_Numpy)


'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0 1 2 3 4 5 6 7 8 9]
[100   1   2   3   4   5   6   7   8   9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
'''