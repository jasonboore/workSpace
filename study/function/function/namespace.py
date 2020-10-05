a = 10
scope = locals()
print(scope)
print(type(scope))
print(scope['a'])
print(a)


def fn():
    a = 10
    scope = locals()
    scope['b'] = 20
    print(scope)


fn()
