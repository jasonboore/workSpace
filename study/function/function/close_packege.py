def fn():
    def inner():
        print('内部函数')

    return inner


r = fn();
r()


# 闭包，操作不想被别人访问的变量
# 形成闭包的条件
# 1.嵌套函数
# 2.将内部函数作为返回值返回
# 3.内部函数必须使用外部函数的变量
def f():
    nums = []

    def average(n):
        nums.append(n)
        return sum(nums) / len(nums)

    return average


ave = f()
print(ave(10))
print(ave(20))
print(ave(30))
