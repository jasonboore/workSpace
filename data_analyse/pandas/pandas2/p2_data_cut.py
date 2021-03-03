import pandas as pd

"""
    实现数据离散化
"""


data = pd.Series([165, 174, 160, 180, 159, 163, 192, 184],
                 index=['No1:165', 'No2:174','No3:160','No4:180','No5:159','No6:163','No7:192','No8:184'])
print(data)
print('-' * 30)

# 1) 分组
# 自动分组
# sr = pd.qcut(data, bins) bins为分成几组
sr = pd.qcut(data, 3)
print(sr)
print('-' * 30)
print(sr.value_counts())
print('-' * 30)
# 2) 将分组好的结果转换成one-hot编码
# pd.get_dummies(sr, prefix=) prefix前缀
one_hot = pd.get_dummies(sr, prefix="身高")
print(one_hot)
print('-' * 30)
# 自定义分组
# sr = pd.cut(data, []]) []区间以列表的形式传进来
bins = [150, 165, 180, 195]
sr2 = pd.cut(data, bins)
print(sr2)
print('-' * 30)
print(sr2.value_counts())
print('-' * 30)
# 2) 将分组好的结果转换成one-hot编码
cut = pd.get_dummies(sr2, prefix="身高")
print(cut)