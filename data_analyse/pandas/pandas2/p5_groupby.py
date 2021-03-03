import pandas as pd
import matplotlib.pyplot as plt
"""
    分组与聚合
"""
col_dic = dict(color=['white', 'red', 'green', 'red', 'green'],
               object=['pen', 'pencil', 'pencil','ashtray','pen'],
               price1=[5.56, 4.20, 1.30, 0.56, 2.75],
               price2=[4.75, 4.12, 1.60, 0.75, 3.15])
col = pd.DataFrame(col_dic)
print(col)
print('-'*50)
# 进行分组，对颜色分组，price1进行聚合
# 用dateFrame的方法进行分组
# max()聚合函数
print(col.groupby(by="color")["price1"].max())
print('-'*50)
# 用Series的方法进行分组
print(col["price1"].groupby(col['color']).max())
print('-'*50)
print('\n')
print('\n')

# 星巴克数据分析
# 1.准备数据
starbucks = pd.read_csv('./directory.csv')
# 按照国家进行分组，求出每个国家星巴克零售店的数量
print(starbucks.groupby("Country").count()['Brand'])
starbucks.groupby("Country").count()['Brand'].sort_values(ascending=False)[:10].plot(kind='bar', figsize=(20, 8), fontsize=40)
# plt.show()
print('-'*30)

# 多索引分组
print(starbucks.groupby(by=["Country", 'State/Province']).count())