#!/usr/bin/env python3
# coding: utf-8
import numpy as np
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
df2 = pd.DataFrame(data1a)

df2["price"] = [150, 120, 100, 300, 150]
print(df2)
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

# 名前による参照
'''
DataFrame型のデータのインデックス、カラム名を使って参照する場合はlocを使用する。
DataFrame型の変数dfに対してdf.loc["インデックスのリスト", "カラムのリスト"]と指定すると、
該当する範囲のDataFrameを得ることができる。
'''
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# DataFrameを生成し、列を追加
df3 = pd.DataFrame()
for column in columns:
  df3[column] = np.random.choice(range(1, 11), 10)
df3.index = range(1, 11)

# loc[]を使ってdfの2行目から5行目までの4行と、"banana", "kiwifruit"の2列を含むDataFrameをdf3に代入する
# インデックスは先頭の行が1、以降は整数値が昇順に付けられている
df4 = df3.loc[range(2,6),["banana","kiwifruit"]]
print(df4)
'''
   banana  kiwifruit
2      10         10
3       9          1
4      10          5
5       5          8
'''

# 番号による参照
'''
インデックス、カラムの番号でDataFrame型のデータを参照する場合はilocを使用する。
DataFrame型の変数dfに対してdf.iloc["行番号のリスト","列番号のリスト"]と指定することで
該当する範囲のDataFrameを得られる。リストを渡す他にスライス機能を使うこともできる。
'''
# iloc[]を使ってdfの2行目から5行目までの4行と、"banana", "kiwifruit"の2列を含むDataFrameをdf3に代入
df5 = df3.iloc[range(1,5), [2, 4]] # スライスを用いて df = df.iloc[1:5, [2, 4]] でも可
print(df5)
'''
   banana  kiwifruit
2      10         10
3       9          1
4      10          5
5       5          8
'''
