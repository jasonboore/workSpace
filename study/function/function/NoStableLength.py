def add(a, b, *c):
    result = a + b
    for i in c:
        result += i
    return result


sum = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(sum)


# 可变参数不是必须写在最后，但是注意，带 * 的参数后的所有参数，必须以关键字参数的形式传递
def add1(a, *b, c):
    result = a + c
    for i in b:
        result += i
    return result


sum = add1(1, 2, 3, c=4)
print(sum)


# 如果在形参的开头直接写一个*，则要求我们的所有的参数必须以关键字参数的形式传递
def add2(*, a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


add2(a=1, b=2, c=3)


# * 只能接受位置参数
def add3(*a):
    print('a =', a)


add3(3)


# **形参可以接收其他的关键字参数，他会将这些参数统一保存到字典当中
# **形参只能有一个，必须写在所有参数的最后
def fn(b, c, **a):
    print('b =', b)
    print('c =', c)
    print('a =', a)
    print(type(a))


fn(a=1, d=8, b=2, c=3, e=9)


def fn11(b, c, **a):
    print('b =', b)
    print('c =', c)
    print('a =', a)
    print(type(a))


fn11(1, 2, e=2, f=3, g=9)


def fn1(a, b, c):
    print('-------------')
    print('b =', b)
    print('c =', c)
    print('a =', a)
    print(type(a))
    print('-----------')


t = 1, 2, 3
# 解包  参数数目需要一致
fn1(*t)
fn1(t, 3, 4)

d = dict(a=100, b=200, c=300)
fn1(**d)


def add4(a, b, *c):
    result = a + b
    for i in c:
        result += i
    return result


x = add4(1, 2)
print(x)
