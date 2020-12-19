import pandas as pd
import numpy as np

# 写入
stack_change = np.random.normal(0, 1, (10, 7))
stock = ['股票{}'.format(i) for i in range(10)]
# 添加列索引
col = ['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', 'open', 'close']
data = pd.DataFrame(stack_change, index=stock, columns=col)
print(data)
data.to_json('test.json', orient='records', lines=True)
# 读取
# sa = pd.read_json('path', orient='records', lines=True)