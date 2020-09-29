my_tuple = ()
print(my_tuple, type(my_tuple))

my_tuple = (1, 2, 3, 47, 5)
print(my_tuple)

my_tuple = 10, 20, 30, 40
print(my_tuple, type(my_tuple))

my_tuple = 50,
print(type(my_tuple))

my_tuple = 10, 20, 30, 40
a, b, c, d = my_tuple
print(a, b, c, d)

a = 100
b = 300
print(f'a = {a}, b = {b}')

# 利用元组交换a和b的值
a, b = b, a
print(f'a = {a}, b = {b}')

a, b = my_tuple[0:2]
print(my_tuple[0:2])
print(a, b)

a, b, *c = my_tuple
print(f'a = {a}, b = {b}, c = {c}')
# 不能同时出现两个以上的*
a, *b, c = my_tuple
# *a, b, c = my_tuple
print(f'a = {a}, b = {b}, c = {c}')