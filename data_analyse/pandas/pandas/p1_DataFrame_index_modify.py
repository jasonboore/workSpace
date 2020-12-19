import numpy as np
import pandas as pd

stack_change = np.random.normal(0, 1, (10, 5))
stock = ['股票{}'.format(i) for i in range(10)]
# 添加列索引
col = pd.date_range(start="20180101", periods=5, freq="B")
stack_change_pd = pd.DataFrame(stack_change, index=stock, columns=col)

# 修改行索引
stock_ = ['股票_{}'.format(i) for i in range(10)]
stack_change_pd.index = stock_
# 重置索引
stack_change_pd = stack_change_pd.reset_index(drop=True)
print(stack_change_pd.head())

# 设置新索引
df = pd.DataFrame(dict(month=[1, 4, 7, 10], year=[2012, 2014, 2012, 2013], sale=[55, 40, 84, 31]))
print(df)
# 以月份设置为新的索引
df = df.set_index("month", drop=False)
print(df)
# 设置多个索引，以年和月份
df = df.set_index(['month', 'year'])
print(df)
print(df.index)