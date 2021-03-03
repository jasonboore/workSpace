import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
 交叉表和透视表
 (探索两个变量之间的关系)
"""

stock = pd.read_csv('./stock_day.csv')

# 星期数据以及涨跌是好是坏数据
# pandas日期类型
data = pd.to_datetime(stock.index)
stock['week'] = data.weekday
# print(stock['week'])

# 准备涨跌幅数据列
stock["pone"] = np.where(stock['p_change'] > 0, 1, 0)
# 交叉表
cross_tab = pd.crosstab(stock['week'], stock["pone"])
# print(cross_tab)
print(cross_tab.div(cross_tab.sum(axis=1), axis=0))
print('*'*30)
cross_tab.div(cross_tab.sum(axis=1), axis=0).plot(kind='bar', stacked=True)
# plt.show()

# 透视表
pivot_tab = stock.pivot_table(['pone'], index=['week'])
print(pivot_tab)