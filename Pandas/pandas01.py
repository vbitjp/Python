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


