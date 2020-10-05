# 高阶函数
# 接收参数作为参数，或者将函数作为返回值的函数是高阶函数


def fn1(i):
    return i % 2 == 0


def fn2(i):
    return i % 3 == 0


def fn3(i):
    return i > 5


def fn(list, func):
    res = []
    for n in list:
        if func(n):
            res.append(n)
    return res


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fn(l, fn3))

# filter() 过滤器，返回可迭代对象满足条件的值
print(list(filter(fn1, l)))

# 匿名函数 lambda表达式
r = list(filter(lambda i: i % 2 == 0, l))
print(r)

# map()函数可以对可迭代对象中的所有元素做指定操作，然后将其添加到一个新的对象中返回
r = list(map(lambda i: i ** 2, l))
print(r)

l = ['aa', 'bbbbb', 'zzzzzz', 'd', 'mmmmm']
# key需要一个函数作为参数，当设置了函数作为参数
# 每次都会以列表的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
l.sort(key=len)
print(l)

l = [1, 8, 6, '5', '3']
l.sort(key=int)
print(l)

# sorted()可以对任意序列进行排序，并且会返回一个新序列

l = [1, 8, 6, '5', '3']
# l = '415615615135153135'
print('排序前：', l)
print(sorted(l, key=int))
print('排序后：', l)