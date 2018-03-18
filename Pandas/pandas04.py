# coding: utf-8
import pandas as pd
'''
# Pandasを用いたCSVの読み込み

df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
#カラム追加
df.columns=["sepal length", "sepal width", "petal length", "petal width", "class"]
print(df)
# csvファイルとしてファイル書き出し
df.to_csv("csv02.csv")

df2 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df2.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium","Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins","Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
print(df2)
df2.to_csv("csv03.csv")

# Pandasを用いたCSVの作成
data = {"OS": ["Machintosh", "Windows", "Linux"],
        "release": [1984, 1985, 1991],
        "country": ["US", "US", ""]}

df3 = pd.DataFrame(data)
df3.to_csv("csv01.csv")
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

# 欠損値の補完 (NaNを0で入れ替えて埋める)
print(sample_data_frame.fillna(0))
'''
          0         1         2         3
0  0.854631  0.454377  0.403951  0.326203
1  0.000000  0.140653  0.317357  0.462611
2  0.224268  0.575320  0.000000  0.206915
3  0.777863  0.318344  0.668449  0.660477
4  0.383075  0.093481  0.745398  0.602430
5  0.333844  0.858233  0.105188  0.000000
6  0.370230  0.806643  0.235804  0.000000
7  0.565755  0.369090  0.174021  0.000000
8  0.532965  0.765538  0.444683  0.000000
9  0.468346  0.525309  0.852663  0.000000
'''

# 欠損値の補完 (NaNを前の行の値に入れ替えて埋める)
print(sample_data_frame.fillna(method="ffill"))
'''
          0         1         2         3
0  0.175973  0.227192  0.498117  0.106192
1  0.175973  0.351884  0.815590  0.503531
2  0.208024  0.067207  0.815590  0.808687
3  0.498118  0.764555  0.587892  0.239512
4  0.054247  0.809377  0.903931  0.778462
5  0.931013  0.276270  0.837106  0.778462
6  0.009442  0.159268  0.992099  0.778462
7  0.578551  0.539334  0.474886  0.778462
8  0.236181  0.344001  0.843000  0.778462
9  0.002803  0.833982  0.423760  0.778462
'''

# 欠損値の補完（平均値代入法
print(sample_data_frame.fillna(sample_data_frame.mean()))
'''
          0         1         2         3
0  0.139880  0.191978  0.755530  0.584762
1  0.498560  0.384348  0.814590  0.530452
2  0.208535  0.324267  0.585750  0.654869
3  0.828496  0.604487  0.543729  0.990833
4  0.182887  0.182064  0.747263  0.309389
5  0.250812  0.907631  0.098280  0.614061
6  0.912519  0.782772  0.628996  0.614061
7  0.674980  0.613285  0.713567  0.614061
8  0.460082  0.075345  0.378732  0.614061
9  0.828851  0.537526  0.591060  0.614061
'''

# キーごとの統計量の算出
df4 = pd.read_csv("csv03.csv")
# キーごとの平均値
print(df4["Alcohol"].mean())
# 13.00061797752809

# キーごとの平均値
print(df4["Magnesium"].mean())
# 99.74157303370787

# 重複データの検出・削除
dupli_data = DataFrame({"col1":[1, 1, 2, 3, 4, 4, 6, 6]
                       ,"col2":["a", "b", "b", "b", "c", "c", "b", "b"]})
print(dupli_data)
'''
   col1 col2
0     1    a
1     1    b
2     2    b
3     3    b
4     4    c
5     4    c
6     6    b
7     6    b
'''
print(dupli_data.duplicated())
'''
0    False
1    False
2    False
3    False
4    False
5     True
6    False
7     True
dtype: bool

duplicatedを用いると、重複のある行にTrueと表示する。出力はSeries型。dtype とは "Data Type" のことで、要素の型。
'''
print(dupli_data.drop_duplicates())
'''
   col1 col2
0     1    a
1     1    b
2     2    b
3     3    b
4     4    c
6     6    b

drop_duplicatesを用いると、重複したデータの削除後のデータを表示する。
'''

# マッピング
attri_data1 = {"ID": ["100", "101", "102", "103", "104", "106", "108", "110", "111", "113"]
        ,"city": ["Tokyo", "Osaka", "Kyoto", "Hokkaido", "Tokyo", "Tokyo", "Osaka", "Kyoto", "Hokkaido", "Tokyo"]
        ,"birth_year" :[1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981]
        ,"name" :["Hiroshi", "Akiko", "Yuki", "Satoru", "Steeve", "Mituru", "Aoi", "Tarou", "Suguru", "Mitsuo"]}
attri_data_frame1 = DataFrame(attri_data1)

print(attri_data_frame1)
'''
    ID  birth_year      city     name
0  100        1990     Tokyo  Hiroshi
1  101        1989     Osaka    Akiko
2  102        1992     Kyoto     Yuki
3  103        1997  Hokkaido   Satoru
4  104        1982     Tokyo   Steeve
5  106        1991     Tokyo   Mituru
6  108        1988     Osaka      Aoi
7  110        1990     Kyoto    Tarou
8  111        1995  Hokkaido   Suguru
9  113        1981     Tokyo   Mitsuo
'''

# 新しい辞書を作成
city_map ={"Tokyo":"Kanto"
          ,"Hokkaido":"Hokkaido"
          ,"Osaka":"Kansai"
          ,"Kyoto":"Kansai"}

# 新しいカラムとしてregionを追加
attri_data_frame1["region"] = attri_data_frame1["city"].map(city_map)

print(attri_data_frame1)
'''
    ID  birth_year      city     name    region
0  100        1990     Tokyo  Hiroshi     Kanto
1  101        1989     Osaka    Akiko    Kansai
2  102        1992     Kyoto     Yuki    Kansai
3  103        1997  Hokkaido   Satoru  Hokkaido
4  104        1982     Tokyo   Steeve     Kanto
5  106        1991     Tokyo   Mituru     Kanto
6  108        1988     Osaka      Aoi    Kansai
7  110        1990     Kyoto    Tarou    Kansai
8  111        1995  Hokkaido   Suguru  Hokkaido
9  113        1981     Tokyo   Mitsuo     Kanto

regionカラムに地方名が追加された
'''
# また新しい辞書を作成
we_map ={"Tokyo":"east"
          ,"Hokkaido":"east"
          ,"Osaka":"west"
          ,"Kyoto":"west"}
# 新しいカラムとしてWEを追加
attri_data_frame1["WE"] = attri_data_frame1["city"].map(we_map)
print(attri_data_frame1)
'''
    ID  birth_year      city     name    region    WE
0  100        1990     Tokyo  Hiroshi     Kanto  east
1  101        1989     Osaka    Akiko    Kansai  west
2  102        1992     Kyoto     Yuki    Kansai  west
3  103        1997  Hokkaido   Satoru  Hokkaido  east
4  104        1982     Tokyo   Steeve     Kanto  east
5  106        1991     Tokyo   Mituru     Kanto  east
6  108        1988     Osaka      Aoi    Kansai  west
7  110        1990     Kyoto    Tarou    Kansai  west
8  111        1995  Hokkaido   Suguru  Hokkaido  east
9  113        1981     Tokyo   Mitsuo     Kanto  east
'''

# ビン分割:ある離散的な範囲にデータを分割して集計する機能
# 分割の粒度リスト
birth_year_bins = [1980,1985,1990,1995,2000]
# ビン分割
birth_year_cut_data = pd.cut(attri_data_frame1.birth_year,birth_year_bins)
print(birth_year_cut_data)
'''
0    (1985, 1990]
1    (1985, 1990]
2    (1990, 1995]
3    (1995, 2000]
4    (1980, 1985]
5    (1990, 1995]
6    (1985, 1990]
7    (1985, 1990]
8    (1990, 1995]
9    (1980, 1985]
Name: birth_year, dtype: category
Categories (4, interval[int64]): [(1980, 1985] < (1985, 1990] < (1990, 1995] < (1995, 2000]]
()はその値を含まず、[]はその値を含む。つまり(1980, 1985]の場合、1980は含まず1985は含む
'''

# それぞれのビンの数を集計したい場合は、value_countsを使う
print(pd.value_counts(birth_year_cut_data))
'''
(1985, 1990]    4
(1990, 1995]    3
(1980, 1985]    2
(1995, 2000]    1
Name: birth_year, dtype: int64
'''

# それぞれのビンに名前をつける
group_names = ["first1980", "second1980", "first1990", "second1990"]
birth_year_cut_data = pd.cut(attri_data_frame1.birth_year,birth_year_bins,labels = group_names)
print(pd.value_counts(birth_year_cut_data))
'''
second1980    4
first1990     3
first1980     2
second1990    1
Name: birth_year, dtype: int64
'''

# あらかじめ分割数を指定して分割(同じサイズのビンを作成)
print(pd.cut(attri_data_frame1.birth_year,2))
'''
0      (1989.0, 1997.0]
1    (1980.984, 1989.0]
2      (1989.0, 1997.0]
3      (1989.0, 1997.0]
4    (1980.984, 1989.0]
5      (1989.0, 1997.0]
6    (1980.984, 1989.0]
7      (1989.0, 1997.0]
8      (1989.0, 1997.0]
9    (1980.984, 1989.0]
Name: birth_year, dtype: category
Categories (2, interval[float64]): [(1980.984, 1989.0] < (1989.0, 1997.0]]
'''
