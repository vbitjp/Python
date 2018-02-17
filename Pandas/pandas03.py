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
