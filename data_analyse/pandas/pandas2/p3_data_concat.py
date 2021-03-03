import pandas as pd
"""
    数据合并
"""

# 1)按方向拼接

data = pd.Series([165, 174, 160, 180, 159, 163, 192, 184],
                 index=['No1:165', 'No2:174','No3:160','No4:180','No5:159','No6:163','No7:192','No8:184'])
print(data)
sr = pd.qcut(data, 3)
print(sr)
cut = pd.get_dummies(sr, prefix="身高")
print(cut)
print('-' * 30)
# 水平拼接
con = pd.concat([data, cut], axis=1)
print(con)
print('-' * 30)
# 竖直拼接
con = pd.concat([data, cut], axis=0)
print(con)
print('-' * 30)
print('\n')
print('\n')
print('\n')
# 按照索引拼接（常用）
dic_left = dict(Key1=['K0', 'K0','K1','K2'],
                Key2=['K0', 'K1','K0','K1'],
                A=['A0', 'A1','A2','A3'],
                B=['B0', 'B1','B2','B3'])
left = pd.DataFrame(dic_left)

dic_right = dict(Key1=['K0', 'K1','K1','K2'],
                Key2=['K0', 'K0','K0', 'K0'],
                C=['C0', 'C1','C2','C3'],
                D=['D0', 'D1','D2','D3'])

right = pd.DataFrame(dic_right)


print(left)
print('-' * 30)
print(right)
print('-' * 30)
# 内连接用的比较多
data_inner_mer = pd.merge(left, right, how='inner', on=['Key1', 'Key2'])
print(data_inner_mer)
print('-' * 30)
data_left_mer = pd.merge(left, right, how='left', on=['Key1', 'Key2'])
print(data_left_mer)
print('-' * 30)
data_right_mer = pd.merge(left, right, how='right', on=['Key1', 'Key2'])
print(data_right_mer)
print('-' * 30)
data_outer_mer = pd.merge(left, right, how='outer', on=['Key1', 'Key2'])
print(data_outer_mer)
print('-' * 30)