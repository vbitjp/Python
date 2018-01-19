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

