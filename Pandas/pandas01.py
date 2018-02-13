#!/usr/bin/env python3
# coding: utf-8

import pandas as pd

fruits = {"banana": 3, "orange": 2}
print(pd.Series(fruits))
'''
banana    3
orange    2
dtype: int64
'''

# Series用のラベル作成（インデックス）
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# Series用のデータ値の代入
data = [10, 5, 8, 12, 3]

# Series作成
series = pd.Series(data, index=index)


# 辞書型を用いてDataFrame用のデータの作成
data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}

# DataFrame作成
df = pd.DataFrame(data)

print("Seriesデータ")
print(series)
print()
print("DataFrameデータ")
print(df)

'''
Seriesデータ
apple         10
orange         5
banana         8
strawberry    12
kiwifruit      3
dtype: int64

DataFrameデータ
       fruits  time  year
0       apple     1  2001
1      orange     4  2002
2      banana     5  2001
3  strawberry     6  2008
4   kiwifruit     3  2006
'''
'''
Pandasのデータ構造のうちの1つであるSeriesは1次元の配列のように扱う。
データとそれに関連付けたインデックスを指定することでもSeriesを生成できる。
pandas.Series(データ配列, index=インデックス配列)
インデックスを指定しない場合は0から順の整数がインデックスとして付く。
Seriesを出力した際に「dtype: int64」と出力されるが、Seriesに格納されている値が ”int64”
という型であることを示している。dtype とは “Data type” のことで、データの型を指す。
(データが整数であれば“int”、少数点を持つものであれば“float” など)int64 とは64bitのサイズを持つ整数
-2^{32} ~ 2^{32 - 1}
​​ までの整数を扱うことができる。dtype には他にも int32 など同じ整数でもサイズの異なるものや、
0か1のみを値に持つ bool という型などがある。
'''

fruits = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}
series = pd.Series(fruits)
print(series[0:4])
'''
banana    3
grape     1
orange    4
peach     5
dtype: int64
'''
print(series[["orange", "peach"]])
'''
orange    4
peach     5
dtype: int64
'''

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)

# インデックス参照を用いてseriesの2つ目から4つ目までの3つの要素をスライス
print(series[1:4])
'''
orange         5
banana         8
strawberry    12
dtype: int64
'''
# "apple", "banana", "kiwifruit"のインデックスを持つ要素取り出し
print(series[["apple", "banana", "kiwifruit"]])
'''
apple        10
banana        8
kiwifruit     3
dtype: int64
'''
# seriesのデータのみ取り出す(.valuesメソッド)
print(series.values)
# [10  5  8 12  3]

# seriesのインデックスのみ取り出す(.indexメソッド)
print(series.index)
# Index(['apple', 'orange', 'banana', 'strawberry', 'kiwifruit'], dtype='object')

# 要素追加
print(series.append(pd.Series([12], index=["pineapple"])))
'''
apple         10
orange         5
banana         8
strawberry    12
kiwifruit      3
pineapple     12
dtype: int64
'''

# 要素削除
print(series.drop("strawberry"))
'''
apple        10
orange        5
banana        8
kiwifruit     3
dtype: int64
'''

# booleanによる要素取り出し
conditions = [True, True, False, False, False]
print(series[conditions])
'''
apple     10
orange     5
dtype: int64
'''

# 条件式による要素取り出し
print(series[series >= 5])
'''
apple         10
orange         5
banana         8
strawberry    12
dtype: int64
'''

# series内の要素のうち、値が5以上10未満の要素を取り出す
print(series[series >= 5][series < 10])
'''
orange    5
banana    8
dtype: int64
'''

# インデックスについてアルファベット順(昇順)にソート
print(series.sort_index())
'''
apple         10
banana         8
kiwifruit      3
orange         5
strawberry    12
dtype: int64
'''
# インデックスについて降順にソート
print(series.sort_index(ascending=False))
'''
strawberry    12
orange         5
kiwifruit      3
banana         8
apple         10
dtype: int64
'''
# データについて値の大きさを昇順にソート
print(series.sort_values())
'''
kiwifruit      3
orange         5
banana         8
apple         10
strawberry    12
dtype: int64
'''
# データについて値の大きさを降順にソート
print(series.sort_values(ascending=False))
'''
strawberry    12
apple         10
banana         8
orange         5
kiwifruit      3
dtype: int64
'''