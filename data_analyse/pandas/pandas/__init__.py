import numpy as np
import pandas as pd

stack_change = np.random.normal(0, 1, (10, 5))
# print(stack_change)
# 使用DataFrame
# 添加行索引
stock = ['股票{}'.format(i) for i in range(10)]
# 添加列索引
col = pd.date_range(start="20180101", periods=5, freq="B")
stack_change_pd = pd.DataFrame(stack_change, index=stock, columns=col)
print(stack_change_pd)

# 属性
# shape
print(stack_change_pd.shape)

# index 行索引
print(stack_change_pd.index)
# columes 列索引
print(stack_change_pd.columns)
# values 值
print(stack_change_pd.values)
# T 转置
print(stack_change_pd.T)

# 方法
# head 前三行
print(stack_change_pd.head(3))

# tail 后五行
print(stack_change_pd.tail(5))

