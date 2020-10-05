help(print)


def f(a: int, b: bool, c: str = "int") -> str:
    """
    这是一个文档字符串的示例
    :param a:作用，类型，默认值。。。
    :param b:作用，类型，默认值。。。
    :param c:作用，类型，默认值。。。
    :return:作用，类型，默认值。。。
    """


# 变量作用域
# 内层变量可以访问外层变量
def f2():
    a = 3

    def f3():
        print('a =', a)

    f3()


f2()

a = 10


def f4():
    # 如果希望在函数内部修改全局变量。使用global声明变量
    # 此时再去修改时，就是修改全局
    global a
    a = 20
    print('函数内部：', a)


f4()
print('函数外部：', a)


