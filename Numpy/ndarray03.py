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