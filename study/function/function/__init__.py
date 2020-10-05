def multiple(a, b, c):
    print(a, '*', b, '*', c, '= ', a * b * c)


def welcome(name):
    print('北京欢迎您！', name, "!")


multiple(21, 58, 69)
welcome('张三')


def f(a, b, c=30):
    print('a =', a)
    print('b = ', b)
    print('c = ', c)


f(1, 2)

f(b=2, c=3, a=5)

f(1, b=1)


def fn2(a):
    a[0] = 30
    print('a = ', a)


c = [4, 5, 6]
fn2(c)
print('c = ', c)
