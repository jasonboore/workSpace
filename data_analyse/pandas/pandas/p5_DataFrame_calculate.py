import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stack_change = np.random.normal(0, 1, (10, 7))
stock = ['股票{}'.format(i) for i in range(10)]
# 添加列索引
col = ['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', 'open', 'close']
data = pd.DataFrame(stack_change, index=stock, columns=col)
print(data)
# 算数运算
# data['2018-01-01'] = data['2018-01-01'] + 3
# data['2018-01-01'] = data['2018-01-01'].add(3)
# print(data.head(3))
# data = data - 10
# print(data)
# data = data * 5
# print(data)
# data['2018-01-01'] = data['2018-01-01'].sub(data['2018-01-02'])
# print(data)

# 逻辑运算
## 逻辑运算符
data1 = data[data['2018-01-01'] > 0]
print(data1)
data2 = data[(data['2018-01-01'] > 0) & (data['2018-01-02'] < 1)]
print(data2)
data3 = data[(data['2018-01-01'] > 0) | (data['2018-01-02'] < 1)]
print(data3)
## 逻辑运算函数
print('-' * 30)
data1 = data.query("open > 0 & close < 1")
print(data1)

print('-' * 30)
data.iloc[0][5] = 0.474013
data.iloc[1][5] = 0.178138
print(data['open'].isin([0.474013, 0.178138]))
# 统计运算
print('-' * 30)
data_analyse = data.describe()
print(data_analyse)
print('-' * 30)
max_col = data.max()
max_row = data.max(axis=1)
print(max_col)
print('-' * 30)
max_col_index = data.idxmax()
min_row_index = data.idxmin(axis=1)
print(max_col_index)

## 累计统计函数
print('-' * 30)
cumsum_open = data['open'].sort_index().cumsum()  # 截止到第N只股票的累计金额
# cumsum_open.plot()
# plt.figure()
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.plot(cumsum_open)
# plt.show()
print(cumsum_open)
# 自定义运算
print('-' * 30)
data4 = data.apply(lambda x: x.max() - x.min())
data5 = data[['open']].apply(lambda x: x.max() - x.min())
print(data['open'].max() - data['open'].min())
print(data5)

# Pandas画图
data.plot(x='open', y='close', kind='scatter')
plt.show()
