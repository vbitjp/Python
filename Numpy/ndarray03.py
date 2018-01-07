#!/usr/bin/env python3
# coding: utf-8
'''
ブールインデックス参照
'''
import numpy as np

arr = np.array([2, 4, 6, 8, 10]) 
print(arr[np.array([True, True, True, False, True])])  
arr = np.arange(16) 
print(arr[arr % 3 == 1])
print(arr[(arr % 3 == 0) + (arr % 5 == 0)])
print(arr[(arr % 3 == 0) * (arr % 5 == 0)])


arr = np.array([2, 3, 4, 5, 6, 7])
# 変数arrの各要素が2で割り切れるかどうかを示す真偽値の配列を出力
print(arr % 2 == 0)
# 変数arr各要素のうち2で割り切れる要素の配列を出力
print(arr[arr % 2 == 0])

arr = np.array([4, -9, 16, -4, 20])
print(arr)

# 変数arrの各要素を絶対値にして、変数arr_absに代入
arr_abs = np.abs(arr)
print(arr_abs)

# 変数arr_absの各要素のeのべき乗と平方根を出力
print(np.exp(arr_abs))
print(np.sqrt(arr_abs))

'''
[ 4 -9 16 -4 20]
[ 4  9 16  4 20]
[  5.45981500e+01   8.10308393e+03   8.88611052e+06   5.45981500e+01
   4.85165195e+08]
[ 2.          3.          4.          2.          4.47213595]
'''

arr1 = [2, 5, 7, 9, 5, 2]
arr2 = [2, 5, 8, 3, 1]

# unique()関数を用いて重複をなくした配列を変数new_arr1に代入
new_arr1 = np.unique(arr1)
print(new_arr1)

# 変数new_arr1と変数arr2の和集合を出力
print(np.union1d(new_arr1, arr2))

# 変数new_arr1と変数arr2の積集合を出力
print(np.intersect1d(new_arr1, arr2))

# 変数new_arr1から変数arr2を引いた差集合を出力
print(np.setdiff1d(new_arr1, arr2))

'''
[2 5 7 9]
[1 2 3 5 7 8 9]
[2 5]
[7 9]
'''

from numpy.random import randint

# 変数arr1に各要素が0~10までの整数の行列(5×2)を代入
arr1 = randint(0, 11, (5, 2))
print(arr1)

# 変数arr2に0~1までの一様乱数を三つ代入し
arr2 = np.random.rand(3)
print(arr2)
'''
[[5 8]
 [9 2]
 [2 8]
 [8 4]
 [9 4]]
[ 0.01650348  0.57153792  0.56771237]
'''

# 二次元配列
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)

# 変数arrの行列の各次元ごとの要素数を出力
print(arr.shape)

# 変数arrを2行4列から4行2列の行列に形状変換(転置行列ではない)
print(arr.reshape(4, 2))

'''
[[1 2 3 4]
 [5 6 7 8]]

(2, 4)

[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''

# 行列から要素抜き出し

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

# 変数arrの要素のうち3のみ出力
print(arr[0, 2])

# 変数arrから取り出して出力
print(arr[1:, 0:2])

'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
3
[[4 5]
 [7 8]]
'''

arr = np.array([[1, 2, 3], [4, 5, 12], [15, 20, 22]])

# 単純な合計値のスカラー
print(arr.sum())

# 列方向に積算した1次元配列を求める
print(arr.sum(axis=0))

# 行方向に積算した1次元配列を求める
print(arr.sum(axis=1))
'''
84
[20 27 37]
[ 6 21 57]
'''

'''
ファンシーインデックス参照
あるndarray配列に対してその順番を示す配列をインデックス参照として渡すと
特定の順序で行を抽出して返す
'''

arr = np.arange(25).reshape(5, 5)

# 変数arrの行の順番を変更して配列を返す
print(arr)
print(arr[[1, 3, 0]])

'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]

[[ 5  6  7  8  9]
 [15 16 17 18 19]
 [ 0  1  2  3  4]]
'''

arr = np.arange(10).reshape(2, 5)

# 変数arrを転置行列を得る
print(np.transpose(arr))
# Tメソッドでも同じ結果を得る
print(arr.T)
'''
[[0 5]
 [1 6]
 [2 7]
 [3 8]
 [4 9]]
[[0 5]
 [1 6]
 [2 7]
 [3 8]
 [4 9]]
'''

arr = np.array([[8, 4, 2], [3, 5, 1]])

# argsort関数=ソート後のインデックスを返す
print(arr.argsort())

# np.sort()を用いてソート
print(np.sort(arr))

# 行でソート(ソートした配列のコピーを返す)
arr.sort(0)
print(arr)

# 列でソート(ソートした配列のコピーを返す)
arr.sort(1)
print(arr)

'''
*
[[2 1 0]
 [2 0 1]]
元の行列1行目[8, 4, 2]をインデックス付きで表すと[8(0), 4(1), 2(0)]となる。
ソートされると[2(0), 4(1), 8(0)]なので、対応したインデックス値[2 1 0]が返される。
2行目[3, 5, 1]も同様にインデックス付きで表すと[3(0), 5(1), 1(2)]であり、
ソートされると[1(2), 3(0), 5(1)]なので、対応したインデックス値[2 0 1]が返される。

*
[[2 4 8]
 [1 3 5]]

*
[[3 4 1]
 [8 5 2]]
元の行列
[[8 4 2]
 [3 5 1]]
 の縦から見て8と3のペアを、降順に3, 8とソート。次に4と5のペアを、降順に4, 5とソート、
 次に2と1のペアをを降順に1, 2とソートした

*
[[1 3 4]
 [2 5 8]]
元の行列
[[8 4 2]
 [3 5 1]]
 のうち、
[8 4 2]をソートして[2 4 8]を得て、[3 5 1]をソートして[1 3 5]を得た
'''

arr = np.arange(9).reshape(3, 3)
print(arr)

# 変数arrとarrの行列積
print(arr.dot(arr)) # dotはx.dot(y)関数としても使えて
print(np.dot(arr, arr)) # メソッドとしても同じ結果を得る

# 変数vecを1次元で定義
vec = arr.reshape(9)
print(vec)

# 変数vecのノルム(要素の二乗和に対する平方根)出力
print(np.linalg.norm(vec))

'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]

[[ 15  18  21]
 [ 42  54  66]
 [ 69  90 111]]

[[ 15  18  21]
 [ 42  54  66]
 [ 69  90 111]]

[0 1 2 3 4 5 6 7 8]

14.2828568571
'''

arr = np.arange(15).reshape(3, 5)
print(arr)
# arrの列ごとの平均
print(arr.mean(axis=0))

# arrの行の合計
print(arr.sum(axis=1))

# arrの最小値
print(arr.min())

# arrのそれぞれの列の最大値のインデックス
print(arr.argmax(axis=0))

'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

[ 5.  6.  7.  8.  9.]

[10 35 60]

0

[2 2 2 2 2]
'''

x = np.arange(9).reshape(3, 3)
print(x)
print(x + 1) # 配列のブロードキャスト。要素全てに1を加算する
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]

[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

# 0から14の整数値をもつ3×5のNumpy配列xを生成
x = np.arange(15).reshape(3, 5)
print(x)

# 0から4の整数値をもつ1×5のNumpy配列yを生成
y = np.array([np.arange(5)])
print(y)

# xのn番目の列のすべての行からnだけ引く(配列のブロードキャスト)
print(x - y)

'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

[[0 1 2 3 4]]

[[ 0  0  0  0  0]
 [ 5  5  5  5  5]
 [10 10 10 10 10]]
'''

