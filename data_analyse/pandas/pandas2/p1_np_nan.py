import pandas as pd
import numpy as np

# 如何处理NaN
movie = pd.read_csv("./IMDB-Movie-Data.csv")
# print(movie)
# 判断是否存在缺失值
IS_NUll = pd.isnull(movie)
# 返回True  说明数据集中存在缺失值
print(np.any(IS_NUll))
print('-'*32)
IS_NUll = pd.notnull(movie)
# 返回false 说明数据集中存在缺失值
print(np.all(IS_NUll))
print('-'*32)
print(pd.isnull(movie).any())
print('-'*32)
print(pd.notnull(movie).all())
print('-'*32)
# 如何处理缺失值?
## 删除存在缺失值的数据(数据量比较大时用)
data1 = movie.dropna()
print(pd.isnull(data1).any())
print('-'*32)

# Revenue (Millions)     True
# Metascore              True
## 替换缺失值(数据量比较小)
movie['Revenue (Millions)'].fillna(movie['Revenue (Millions)'].mean(), inplace=True)
movie['Metascore'].fillna(movie['Metascore'].mean(), inplace=True)
print(pd.isnull(movie).any())
print('-'*32)



# 如何处理带有特殊标记的
#  通过网址获得数据
# path = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
names = ['Sample code number',
         'Clump Thickness',
         'Uniformity of Cell Size',
         'Uniformity of Cell Shape',
         'Marginal Adhesion ',
         'Single Epithelial Cell Size',
         'Bare Nuclei',
         'Bland Chromatin ',
         'Normal Nucleoli',
         'Mitoses',
         'Class']
data = pd.read_csv('breast-cancer-wisconsin.data', names=names)
print(data.head())
print('*'*80)
# 替换 (? -> NaN)
data_new = data.replace('?', value=np.nan)
print(data_new.head())
print('*'*80)
# 删除缺失值
data_new.dropna(inplace=True)
print(data_new.isnull().any())





