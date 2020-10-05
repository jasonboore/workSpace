def factorial(n):
    """
    该函数求任意数的阶乘
    :param n:要求求得数的阶乘
    :return:
    """
    if n < 2:
        return 1
    return n * factorial(n - 1)


print(factorial(10))


def power(n, i):
    if i == 0:
        return 1
    return n * power(n, i - 1)


print(power(2, 10))


def isPar(str, start, end):
    if start >= end:
        return True
    return str[start] == str[end] and isPar(str, start + 1, end - 1)

def isPar2(str):
    if(len(str) < 2):
        return True
    return str[0] == str[-1] and isPar2(str[1: -1])


str = 'abcdefedcba'
print(isPar(str, 0, -1))
print(isPar2(str))
