import pandas as pd

data = pd.read_csv('../pandas2/stock_day.csv')
data = data.drop(['ma5', 'ma10'], axis=1)

# 索引操作
## 直接索引(必须先列后行)
data1 = data['open']['2018-02-26']
print(data1)
## 按名字索引
data2 = data.loc['2018-02-26']['open']
print(data2)
data2 = data.loc['2018-02-26', 'open']
print(data2)
## 按数字索引
data3 = data.iloc[1, 0]
print(data3)


## 组合索引（数字、名字）
# data4 = data._ix[0:4, ['open', 'close', 'high']]
# 推荐使用loc和iloc来获取
print(data.loc[data.index[:4], ['open', 'close', 'high']])
print('-'*30)
print(data.iloc[:4, data.columns.get_indexer(['open', 'close', 'high'])])

# 赋值操作
# 这一列所有值全变成100
data.open = 100
print(data)
data['open'] = 200
print(data)
data.iloc[1, 0] = 8888
print('-'*30)
print(data)
print('-'*30)
print('-'*30)
# 排序

## 对内容进行排序
### 按最高价从大到小排列
data = data.sort_values(by='high', ascending=False)
print('-'*30)
print(data)
data = data.sort_values(by= ['high', 'p_change'])
print('-'*30)
print(data)

## 对索引进行排序
print(data.sort_index())

price = data['price_change']
print(price.sort_values())