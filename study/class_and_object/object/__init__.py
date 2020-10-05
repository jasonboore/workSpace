a = str('hello')
b = int(10)
print(a, type(a))
print(b, type(b))


# class 类名([父类]):
#     代码块
# 没有父类可省略括号
class MyClass:
    pass


o1 = MyClass()
print(o1, type(o1))

print(id(MyClass), type(MyClass))

o1.name = '孙悟空'
print(o1.name)


class Person:
    name = '孙悟空'

    def say_hello(self):
        print('你好', self.name)


swk = Person()
swk.name = 'swk'
swk.say_hello()
