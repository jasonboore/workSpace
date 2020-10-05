class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__这个特殊方法会在尝试将对象转换为字符串的时候调用
    # 作用：可以指定对象转化为字符串的结果
    def __str__(self):
        return f'Person [name = {self.name}, age = {self.age}]'

    # 这个特殊方法会在对当前对象使用repr()函数时调用
    # 作用：指定对象在'交互模式'中直接输出的结果
    def __repr__(self):
        return 'hello'

    # object:__lt__(self, other) 小于 <
    # object: __le__(self, other) 小于等于 <=
    # object: __eq__(self, other) 等于 ==
    # object: __ne__(self, other) 不等于 !=
    # object: __gt__(self, other) 大于 >
    # object: __ge__(self, other) 大于等于 >=
    # 小于一边为self
    def __lt__(self, other):
        print(self.name)
        return self.age < other.age


    def __bool__(self):
        return self.name != ""



p1 = Person('孙悟空', 18)
p2 = Person('猪八戒', 50)
p3 = Person('', 20)
# 当我们打印一个对象时，实际上打印的是对象中的特殊方法，__srt__()的返回值
print(p1)

print(p1 > p2)
print(bool(p3))