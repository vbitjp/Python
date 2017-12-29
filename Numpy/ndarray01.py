#!/usr/bin/env python
# coding: utf-8
'''
本コードは http://www.python-izm.com/contents/numerical/numpy/ndarray.shtml
の記載分を3系に書き換えてパラメータを多少変更した
'''
import numpy

'''
ndarrayはpython本来の配列と違い、少し特殊で同じ型の要素しか代入できない
'''

array_like = [[1, 10, 100], [2, 20, 200]]

# ndarrayの作成方法

print('== array ==')
print(numpy.array(array_like))

# 零行列の初期化

print('== zeros / zeros_like ==')
print(numpy.zeros([2, 3]))
print('-------------------')
print(numpy.zeros_like(array_like))

# 1で満たされた行列の初期化

print('== ones / ones_like ==')
print(numpy.ones([5, 6]))
print('-------------------')
print(numpy.ones_like(array_like))

'''
== array ==
[[  1  10 100]
 [  2  20 200]]
== zeros / zeros_like ==
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
-------------------
[[0 0 0]
 [0 0 0]]
== ones / ones_like ==
[[ 1.  1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.  1.]]
-------------------
[[1 1 1]
 [1 1 1]]
'''

# emptyという名の限りなく0に近い値のndarray作成

print('== empty / empty_like ==')
print(numpy.empty([2, 3]))
print('-------------------')
print(numpy.empty_like(array_like))

# 指定数値で終わる連続自然数値のndarray作成

print(numpy.arange(25))

# 指定数値と指定ステップで数列ndarray作成

print(numpy.arange(50, 75, 2))

# 元の配列をキャストしてndarray作成

print(numpy.array(array_like, numpy.float32))


# ndarrayに代入できるデータ型

array_like = [[0, 1, 100]]

print(numpy.array(array_like, numpy.bool_))
print(numpy.array(array_like, numpy.int_))
print(numpy.array(array_like, numpy.intc))
print(numpy.array(array_like, numpy.intp))
print(numpy.array(array_like, numpy.int8))
print(numpy.array(array_like, numpy.int16))
print(numpy.array(array_like, numpy.int32))
print(numpy.array(array_like, numpy.int64))
print(numpy.array(array_like, numpy.uint8))
print(numpy.array(array_like, numpy.uint16))
print(numpy.array(array_like, numpy.uint32))
print(numpy.array(array_like, numpy.uint64))
print(numpy.array(array_like, numpy.float_))
print(numpy.array(array_like, numpy.float16))
print(numpy.array(array_like, numpy.float32))
print(numpy.array(array_like, numpy.float64))
print(numpy.array(array_like, numpy.complex_))
print(numpy.array(array_like, numpy.complex64))
print(numpy.array(array_like, numpy.complex128))


# ndarrayの属性

na = numpy.array([[1, 10, 100], [2, 20, 200]])

# データ型
print('== dtype ==')
print(na.dtype)

# 全要素数
print('== size ==')
print(na.size)

# 1要素あたりのバイト数
print('== itemsize ==')
print(na.itemsize)

# 総バイト数
print('== nbytes ==')
print(na.nbytes)

# 次元数
print('== ndim ==')
print(na.ndim)

# 配列の形状
print('== shape ==')
print(na.shape)

# 次元あたりの総バイト数とバイト数と1要素あたりのバイト数
print('== strides ==')
print(na.strides)

# 実数・虚数（複素数）
print('== real / imag ==')
print(na.real)
print(na.imag)

# 配列の1次元イテレータ
print('== flat ==')
for i in na.flat:
    print(i)

'''
== empty / empty_like ==
[[  4.94065646e-324   4.94065646e-324   4.94065646e-324]
 [  4.94065646e-324   4.94065646e-324   4.94065646e-324]]
-------------------
[[1 1 1]
 [1 1 1]]
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]
[50 52 54 56 58 60 62 64 66 68 70 72 74]
[[   1.   10.  100.]
 [   2.   20.  200.]]
[[False  True  True]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[  0   1 100]]
[[   0.    1.  100.]]
[[   0.    1.  100.]]
[[   0.    1.  100.]]
[[   0.    1.  100.]]
[[   0.+0.j    1.+0.j  100.+0.j]]
[[   0.+0.j    1.+0.j  100.+0.j]]
[[   0.+0.j    1.+0.j  100.+0.j]]
== dtype ==
int64
== size ==
6
== itemsize ==
8
== nbytes ==
48
== ndim ==
2
== shape ==
(2, 3)
== strides ==
(24, 8)
== real / imag ==
[[  1  10 100]
 [  2  20 200]]
[[0 0 0]
 [0 0 0]]
== flat ==
1
10
100
2
20
200
'''