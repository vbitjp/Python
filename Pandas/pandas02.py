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
