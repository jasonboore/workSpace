def add(a, b, c):
    return a + b + c


def mul(a, b):
    return a * b


def fn():
    print('f函数')


def begin_end(old):
    def new_func(*args, **kwargs):
        print(args)
        print(kwargs)
        old(*args, **kwargs)
        print('结束！！')

    return new_func


r = begin_end(add)
r(5, 6, 3)


@begin_end
def fn2():
    print('装饰快捷方法')

fn2()
