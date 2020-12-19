import pandas as pd

data = pd.read_csv('文件路径')
data = data.drop(['ma5', 'ma10', 'ma15'], axis=1)

# 索引操作
## 直接索引(必须先列后行)
data1 = data['open']['2018-02-26']

## 按名字索引
data2 = data.loc['2018-02-26']['open']
data2 = data.loc['2018-02-26', 'open']
## 按数字索引
data3 = data.iloc[1, 0]



## 组合索引（数字、名字）
data4 = data._ix[:4, ['open', 'close', 'high']]
# 推荐使用loc和iloc来获取
data.loc[data.index[:4], ['open', 'close', 'high']]
data.iloc[:4, data.columns.get_indexer(['open', 'close', 'high'])]

# 赋值操作
data.open = 100
data['open'] = 100
data.iloc[1][0] = 222

# 排序

## 对内容进行排序
### 按最高价从大到小排列
data.sort_values(by='high', ascending=False)
data.sort_values(by= ['high', 'p_change'])

## 对索引进行排序
data.sort_index()