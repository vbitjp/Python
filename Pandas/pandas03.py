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