s = {1, 2, 3, 4}
s = {1, 2, 3, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1}
print(s, type(s))

# 创建空集合
s = set()

s = set([1, 2, 3, 7, 6, 5, 1, 45, 165, 8, 5])
s = set('hello')
s = set(dict(name='1', age=18))
print(s, type(s))

s = set([1, 2, 3, 7, 6, 5, 1, 45, 165, 8, 5])
print(list(s)[0])

s.add(10)
print(s)
set1 = {'a', 'b', 'c'}
s.update(set1)
s.update((8, 9, 77, 8, 9, 5, 6, 2, 56, 4684, 8,))
print(s)

# 随机删除几个中的一元素
s.pop()
s.pop()
s.pop()
print(s)
s.remove(45)
print(s)
