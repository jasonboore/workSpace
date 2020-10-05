def add(a, b):
    if a < 0 or b < 0:
        raise Exception('两个参数中不能有负数')
    return a + b

print(add(123,456))
print(add(-1, 6))