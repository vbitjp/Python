#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import pandas as pd

# 指定のインデックスとカラムを持つDataFrameを乱数によって作成する関数
def make_random_df(index, columns, seed):
    np.random.seed(seed)
    df = pd.DataFrame()
    for column in columns:
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df

#インデックス、カラムが一致しているDataFrameの作成
columns = ["apple", "orange", "banana"]
df_data1 = make_random_df(range(1, 5), columns, 0)
df_data2 = make_random_df(range(1, 5), columns, 1)

# df_data1とdf_data2を縦方向に連結
df1 = pd.concat([df_data1, df_data2], axis=0)
print(df1)
'''
   apple  orange  banana
1     45      68      37
2     48      10      88
3     65      84      71
4     68      22      89
1     38      76      17
2     13       6       2
3     73      80      77
4     10      65      72
'''

# df_data1とdf_data2を横方向に連結
df2 = pd.concat([df_data1, df_data2], axis=1)
print(df2)
'''
   apple  orange  banana  apple  orange  banana
1     45      68      37     38      76      17
2     48      10      88     13       6       2
3     65      84      71     73      80      77
4     68      22      89     10      65      72
'''

## インデックス、カラムが一致していないDataFrame同士の連結

columns1 = ["apple", "orange", "banana"]
columns2 = ["orange", "kiwifruit", "banana"]

# インデックスが1,2,3,4, カラムがcolumns1のDataFrameを作成
df_data1 = make_random_df(range(1, 5), columns1, 0)

# インデックスが1,3,5,7, カラムがcolumns2のDataFrameを作成
df_data2 = make_random_df(np.arange(1, 8, 2), columns2, 1)

# df_data1とdf_data2を縦方向に連結
df3 = pd.concat([df_data1, df_data2], axis=0)
print(df3)
'''
   apple  banana  kiwifruit  orange
1   45.0      37        NaN      68
2   48.0      88        NaN      10
3   65.0      71        NaN      84
4   68.0      89        NaN      22
1    NaN      17       76.0      38
3    NaN       2        6.0      13
5    NaN      77       80.0      73
7    NaN      72       65.0      10
'''

# df_data1とdf_data2を横方向に連結
df4 = pd.concat([df_data1, df_data2], axis=1)
print(df4)
'''
   apple  orange  banana  orange  kiwifruit  banana
1   45.0    68.0    37.0    38.0       76.0    17.0
2   48.0    10.0    88.0     NaN        NaN     NaN
3   65.0    84.0    71.0    13.0        6.0     2.0
4   68.0    22.0    89.0     NaN        NaN     NaN
5    NaN     NaN     NaN    73.0       80.0    77.0
7    NaN     NaN     NaN    10.0       65.0    72.0
'''

# 連結する際のラベルの指定
# df_data1とdf_data2を横方向に連結＆Keysに"X", "Y"を指定してMultiIndex化
df5 = pd.concat([df_data1, df_data2], axis=1, keys=["X", "Y"])

#  dfの"Y"ラベルの"banana"抜き出し
Y_banana = df5["Y", "banana"]

print(df5)
'''
      X                    Y                 
  apple orange banana orange kiwifruit banana
1  45.0   68.0   37.0   38.0      76.0   17.0
2  48.0   10.0   88.0    NaN       NaN    NaN
3  65.0   84.0   71.0   13.0       6.0    2.0
4  68.0   22.0   89.0    NaN       NaN    NaN
5   NaN    NaN    NaN   73.0      80.0   77.0
7   NaN    NaN    NaN   10.0      65.0   72.0
'''
print()
print(Y_banana)
'''
1    17.0
2     NaN
3     2.0
4     NaN
5    77.0
7    72.0
Name: (Y, banana), dtype: float64
'''
 
# DataFrameの結合

data1 = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "amount": [1, 4, 5, 6, 3]}
df6 = pd.DataFrame(data1)
print(df6)
print()
'''
   amount      fruits  year
0       1       apple  2001
1       4      orange  2002
2       5      banana  2001
3       6  strawberry  2008
4       3   kiwifruit  2006
'''
data2 = {"fruits": ["apple", "orange", "banana", "strawberry", "mango"],
        "year": [2001, 2002, 2001, 2008, 2007],
        "price": [150, 120, 100, 250, 3000]}
df7 = pd.DataFrame(data2)
print(df7)
print()
'''
       fruits  price  year
0       apple    150  2001
1      orange    120  2002
2      banana    100  2001
3  strawberry    250  2008
4       mango   3000  2007
'''
# "fruits"をKeyに内部結合
df8 = pd.merge(df6, df7, on="fruits", how="inner")
print(df8)
'''
   amount      fruits  year_x  price  year_y
0       1       apple    2001    150    2001
1       4      orange    2002    120    2002
2       5      banana    2001    100    2001
3       6  strawberry    2008    250    2008
'''

# "fruits"をKeyに外部結合
df9 = pd.merge(df6, df7, on="fruits", how="outer")
print(df9)
'''
   amount      fruits  year_x   price  year_y
0     1.0       apple  2001.0   150.0  2001.0
1     4.0      orange  2002.0   120.0  2002.0
2     5.0      banana  2001.0   100.0  2001.0
3     6.0  strawberry  2008.0   250.0  2008.0
4     3.0   kiwifruit  2006.0     NaN     NaN
5     NaN       mango     NaN  3000.0  2007.0
'''

# 荒ぶった列をKeyにして結合する
# 注文情報
order_df = pd.DataFrame([[1000, 2546, 103],
                         [1001, 4352, 101],
                         [1002, 342, 101]],
                         columns=["id", "item_id", "customer_id"])
# 顧客情報
customer_df = pd.DataFrame([[101, "Tanaka"],
                           [102, "Suzuki"],
                           [103, "Kato"]],
                           columns=["id", "name"])

# order_dfとcustomer_dfを結合。order_dfの"customer_id", customer_dfの"id"を参照して内部結合
order_df1 = pd.merge(order_df, customer_df, left_on="customer_id", right_on="id", how="inner")
print(order_df1)
'''
   id_x  item_id  customer_id  id_y    name
0  1000     2546          103   103    Kato
1  1001     4352          101   101  Tanaka
2  1002      342          101   101  Tanaka
'''
# インデックスをKeyにして結合する
customer_df = pd.DataFrame([["Tanaka"],
                           ["Suzuki"],
                           ["Kato"]],
                           columns=["name"])
customer_df.index = [101, 102, 103]
# order_dfとcustomer_dfを結合。order_dfの"customer_id", customer_dfの"id"を参照して内部結合
order_df2 = pd.merge(order_df, customer_df, left_on="customer_id", right_index=True, how="inner")
print(order_df2)
'''
     id  item_id  customer_id    name
0  1000     2546          103    Kato
1  1001     4352          101  Tanaka
2  1002      342          101  Tanaka
'''

# DataFrameを用いたデータ分析

np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# DataFrameを生成し、列を追加
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)

# dfの冒頭3行取得
df_head = df.head(3)
print(df_head)
'''
   apple  orange  banana  strawberry  kiwifruit
1      6       8       6           3         10
2      1       7      10           4         10
3      4       9       9           9          1
'''

# dfの末尾3行取得
df_tail = df.tail(3)
print(df_tail)
'''
    apple  orange  banana  strawberry  kiwifruit
8       6       8       4           8          8
9       3       9       6           1          3
10      5       2       1           2          1
'''

# dfの各要素を2倍
double_df = df * 2
print(double_df)
'''
    apple  orange  banana  strawberry  kiwifruit
1      12      16      12           6         20
2       2      14      20           8         20
3       8      18      18          18          2
4       8      18      20           4         10
5      16       4      10           8         16
6      20      14       8           8          8
7       8      16       2           8          6
8      12      16       8          16         16
9       6      18      12           2          6
10     10       4       2           4          2
'''

# dfの各要素を2乗
square_df = df * df
print(square_df)
'''
    apple  orange  banana  strawberry  kiwifruit
1      36      64      36           9        100
2       1      49     100          16        100
3      16      81      81          81          1
4      16      81     100           4         25
5      64       4      25          16         64
6     100      49      16          16         16
7      16      64       1          16          9
8      36      64      16          64         64
9       9      81      36           1          9
10     25       4       1           4          1
'''

# dfの各要素の平方根
sqrt_df = np.sqrt(df)
print(sqrt_df)
'''
       apple    orange    banana  strawberry  kiwifruit
1   2.449490  2.828427  2.449490    1.732051   3.162278
2   1.000000  2.645751  3.162278    2.000000   3.162278
3   2.000000  3.000000  3.000000    3.000000   1.000000
4   2.000000  3.000000  3.162278    1.414214   2.236068
5   2.828427  1.414214  2.236068    2.000000   2.828427
6   3.162278  2.645751  2.000000    2.000000   2.000000
7   2.000000  2.828427  1.000000    2.000000   1.732051
8   2.449490  2.828427  2.000000    2.828427   2.828427
9   1.732051  3.000000  2.449490    1.000000   1.732051
10  2.236068  1.414214  1.000000    1.414214   1.000000
'''

# 要約統計量を得る
# dfの要約統計量のうち、"mean", "max", "min"を取り出す
df_des = df.describe().loc[["mean", "max", "min"]]
print(df_des)
'''
      apple  orange  banana  strawberry  kiwifruit
mean    5.1     6.9     5.6         4.1        5.3
max    10.0     9.0    10.0         9.0       10.0
min     1.0     2.0     1.0         1.0        1.0
'''
