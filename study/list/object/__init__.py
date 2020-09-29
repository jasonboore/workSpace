s = 'aaa'
print(s, type(s))

s = [1]
print(s, type(s))

a = 5
b = a
print('a = ', id(a), a)
print('b = ', id(b), b)

a = 4
print('a = ', id(a), a)
print('b = ', id(b), b)

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b))
# 比较值是否相等
print(a == b)
# 比较是否是同一对象
print(a is b)
