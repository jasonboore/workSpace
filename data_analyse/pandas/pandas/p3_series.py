import numpy as np
import pandas as pd

stack_change = np.random.normal(0, 1, (10, 5))
stock = ['股票{}'.format(i) for i in range(10)]
# 添加列索引
col = pd.date_range(start="20180101", periods=5, freq="B")
stack_change_pd = pd.DataFrame(stack_change, index=stock, columns=col)

sr = stack_change_pd.iloc[1, :]
# index
print(sr.index)
print(sr.values)

data1 = pd.Series(np.arange(3, 9, 2), index=['a', 'b', 'c'])
print(data1)
data1 = pd.Series(dict(red=100, green=200, blue=500, yellow=1000))
print(data1)
print('-' * 30)
print(sr.sort_values(ascending=False))

print('-' * 30)
print(sr.sort_index(ascending=False))