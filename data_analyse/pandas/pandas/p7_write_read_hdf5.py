import pandas as pd
import numpy as np

# 写入
stack_change = np.random.normal(0, 1, (10, 7))
stock = ['股票{}'.format(i) for i in range(10)]
# 添加列索引
col = ['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', 'open', 'close']
data = pd.DataFrame(stack_change, index=stock, columns=col)
data.to_hdf('test1.h5', key="2018-01-01")
# 读取 只有一个键时不用加key,多个键时需要指定要读的键
data_open = pd.read_hdf('test1.h5', key="open")
print(data_open)

###################################
# 目前tables版本问题，暂时不能用