# coding: utf-8
import pandas as pd

# Pandasを用いたCSVの読み込み

df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
#カラム追加
df.columns=["", "sepal length", "sepal width", "petal length", "petal width", "class"]
print(df)

df2 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df2.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium","Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins","Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
print(df2)