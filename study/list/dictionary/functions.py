d = dict(name='孙悟空', age=18, gender='男')
print(d)

# 双值子序列
d = dict([('name', '孙悟空'), ('age', 1)])
print(d)

print(len(d))
print('name' in d)
print('len' in d)

d['address'] = '花果山'
print(d)
# key存在，则返回key的值
# key不存在，像字典中添加
res = d.setdefault('name', '猪八戒')
res1 = d.setdefault('gender', '男')
print(res1)
print(d)

# 将第二个字典中的值添加到第一个字典，如果出现重复的key，会进行更新
d = dict(a=1, b=2, c=3)
d2 = dict(d=4, e=5, f=6)
d.update(d2)
print(d)

del(d['a'])
print(d)

# 随机删除一个键值对。删除最后一个,按照LIFO
d.popitem()
d.popitem()
print(d)

d = dict(a=1, b=2, c=3)
d2 = dict(d=4, e=5, f=6)
d.update(d2)
d.pop('d')
print(d)
result = d.pop('z', 'default')
print(result)

# 浅复制
d2 = d.copy()
print(id(d), id(d2))

d1 = dict(a=dict(name='孙悟空', age=18), b=2, c=3)
d2 = d1.copy()
d2['a']['name'] = '八戒'
print(d1)
print(d2)

