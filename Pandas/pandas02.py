#!/usr/bin/env python3
# coding: utf-8

import pandas as pd

'''
DataFrameの生成
DataFrameは、Seriesを複数束ねたような2次元のデータ構造をしています。
pandas.DataFrame()に Series を渡すことでDataFrameを生成することができます。
行には0から昇順に番号がつきます。

pandas.DataFrame([Series, Series, ...])
バリューにリスト型を持った辞書型を用いても作成することができます。注意点としては、
リスト型の長さは等しくなくてはいけません。
'''

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)

# series1, seires2からDataFrameを生成する
df = pd.DataFrame([series1, series2])
print(df)
'''
   apple  orange  banana  strawberry  kiwifruit
0     10       5       8          12          3
1     30      25      12          10          8
'''

'''
DataFrameでは、行の名前をインデックス、列の名前をカラムと呼ぶ。
特に指定をしないでDataFrame作成した場合、インデックスは0から
昇順に数字が割り当てられる。また、カラムは元データであるSeries
のindexや辞書型のキーになる。DataFrame型の変数dfのインデックス
はdf.indexに行数と同じ長さのリストを代入することで設定できる。
dfのカラムはdf.columnsに列数と同じ長さのリストを代入することで
設定することができる。
'''

# DataFrame型の変数dfのインデックスを[0, 1]から[1, 2]に変更
df.index = [1, 2]
print(df)
'''
   apple  orange  banana  strawberry  kiwifruit
1     10       5       8          12          3
2     30      25      12          10          8
'''

# 行の追加
'''
新しい観測データや取引情報を得たとき、それらを既存のDataFrameに
追加したい場合がある。DataFrame型の変数dfに対してdf.append("Series型のデータ", ignore_index=True)
を実行すると、渡したSeries型のデータのインデックスがdfのカラムに
対応した上で新しい行が追加されたDataFrameが生成される。
dfのカラムとdfに追加するSeries型のデータのインデックスが一致しない場合、
dfに新しいカラムが追加され、値が存在しない要素はNaNで埋められる。
'''

# 17行目のリスト変数indexにpineappleを追加
index.append("pineapple")
data3 = [30, 12, 10, 8, 25, 3]
series3 = pd.Series(data3, index=index)

# ここで、24行目のDataFrame変数dfにseries3を追加し、dfに再代入してみる
df = df.append(series3, ignore_index=True)
print(df)
'''
   apple  orange  banana  strawberry  kiwifruit  pineapple
0     10       5       8          12          3        NaN
1     30      25      12          10          8        NaN
2     30      12      10           8         25        3.0
'''

data1a = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df1 = pd.DataFrame(data1a)
series = pd.Series(["mango", 2008, 7], index=["fruits", "year", "time"])

df1 = df1.append(series, ignore_index=True)
print(df1)
'''
       fruits  time  year
0       apple     1  2001
1      orange     4  2002
2      banana     5  2001
3  strawberry     6  2008
4   kiwifruit     3  2006
5       mango     7  2008
'''

# 列の追加
'''
DataFrame型の変数dfに対してdf["新しいカラム"]にSeriesもしくはリストを代入することで
新しい列を追加できる。リストを代入した場合は最初行から最初の要素が割り当てられ、Seriesを
代入した場合はSeriesのインデックスがdfのインデックスに対応する。
'''
data1a = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df1 = pd.DataFrame(data1a)

df1["price"] = [150, 120, 100, 300, 150]
print(df1)
'''
       fruits  time  year  price
0       apple     1  2001    150
1      orange     4  2002    120
2      banana     5  2001    100
3  strawberry     6  2008    300
4   kiwifruit     3  2006    150
'''
# ここで、24行目のDataFrame変数dfに新しい列"mango"をnew_columnのデータと共に追加し、dfに再代入してみる
new_column = pd.Series([15, 7], index=[0, 1])
df["mango"] = new_column
print(df)
'''
   apple  orange  banana  strawberry  kiwifruit  pineapple  mango
0     10       5       8          12          3        NaN   15.0
1     30      25      12          10          8        NaN    7.0
2     30      12      10           8         25        3.0    NaN
'''

