# coding: utf-8
import pandas as pd
'''
# Pandasを用いたCSVの読み込み

df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
#カラム追加
df.columns=["sepal length", "sepal width", "petal length", "petal width", "class"]
print(df)

df2 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df2.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium","Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins","Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
print(df2)

# Pandasを用いたCSVの作成
data = {"OS": ["Machintosh", "Windows", "Linux"],
        "release": [1984, 1985, 1991],
        "country": ["US", "US", ""]}

df = pd.DataFrame(data)
df.to_csv("csv01.csv")
'''

# 与えられた2つのDataFrameを結合した、DataFrameはIDが昇順に、列番号も昇順になるよう結合＆出力
from pandas import Series, DataFrame

attri_data1 = {"ID": ["100", "101", "102", "103", "104", "106", "108", "110", "111", "113"],
               "city": ["Tokyo", "Osaka", "Kyoto", "Hokkaido", "Tokyo", "Tokyo", "Osaka", "Kyoto", "Hokkaido", "Tokyo"],
               "birth_year": [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
               "name": ["Hiroshi", "Akiko", "Yuki", "Satoru", "Steeve", "Mituru", "Aoi", "Tarou", "Suguru", "Mitsuo"]}
attri_data_frame1 = DataFrame(attri_data1)

attri_data2 = {"ID": ["107", "109"],
               "city": ["Sendai", "Nagoya"],
               "birth_year": [1994, 1988]}
attri_data_frame2 = DataFrame(attri_data2)

print(attri_data_frame1.append(attri_data_frame2).sort_values(
    by="ID", ascending=True).reset_index(drop=True))

# リストワイズ/ペアワイズ削除(欠損値の扱い)
import numpy as np
from numpy import nan as NA

sample_data_frame = pd.DataFrame(np.random.rand(10,4))

# 試しに一部のデータをわざと欠損させる
sample_data_frame.iloc[1,0] = NA
sample_data_frame.iloc[2,2] = NA
sample_data_frame.iloc[5:,3] = NA

print(sample_data_frame)
'''
          0         1         2         3
0  0.624742  0.582226  0.903410  0.492425
1       NaN  0.391110  0.438770  0.219968
2  0.276040  0.333182       NaN  0.100146
3  0.435066  0.478193  0.363539  0.980547
4  0.905236  0.246206  0.869018  0.239057
5  0.492207  0.511444  0.209087       NaN
6  0.569442  0.518076  0.525844       NaN
7  0.955035  0.170361  0.637786       NaN
8  0.161210  0.985880  0.161823       NaN
9  0.431329  0.154183  0.317345       NaN
'''

print(sample_data_frame.dropna())
'''
データ欠損のある行（NaNを含む行）をまるごと消去することをリストワイズ削除という.
dropna()メソッドでNaNを含む行を削除できる
          0         1         2         3
0  0.732660  0.849580  0.873196  0.177288
3  0.935729  0.682220  0.068760  0.380573
4  0.082761  0.624931  0.456848  0.291219
'''

print(sample_data_frame[[0,1]].dropna())
'''
なるべく利用可能なデータのみ用いたい場合、欠損の少ない列（例: 0列目と1列目）だけを残すことをペアワイズ削除という。
          0         1
0  0.828776  0.259787
2  0.019889  0.244076
3  0.139363  0.007597
4  0.188059  0.297370
5  0.891974  0.004285
6  0.453771  0.234144
7  0.725461  0.975968
8  0.053350  0.526558
9  0.954610  0.194394
'''


