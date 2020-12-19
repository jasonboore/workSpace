import pandas as pd
import numpy as np

stack_change = np.random.normal(0, 1, (10, 7))
stock = ['股票{}'.format(i) for i in range(10)]
# 添加列索引
col = ['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', 'open', 'close']
data = pd.DataFrame(stack_change, index=stock, columns=col)
data.to_csv('./股票.csv')
data.to_csv('股票1.csv', columns=['open', 'close'], mode='a')
data.to_csv('股票2.csv', index=False, header=False, columns=['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05'])
# usecols选择列
# names 给数据加上列索引(在只有数据，没有列索引的情况下)
data = pd.read_csv('./股票.csv', usecols=["open", "close"])
print(data)
data = pd.read_csv('./股票2.csv', names=['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05'])
print(data)
