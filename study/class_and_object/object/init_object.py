# class 类名([父类]):
#     公共属性
#     def __init__(self):
#         ...
#      其他的方法
#       def method_1(self, ...):
#           ....
# 没有父类可省略括号
class Person:
    # 代码块在加载类时执行
    # print('我是代码块 ！')

    def __init__(self, name):
        """
        初始化方法，创建对象是自动调用
        """
        print('__init__执行了！')
        self.name = name

    def say_hello(self):
        print('你好%s' % self.name)


p1 = Person('swk')
p2 = Person('zbj')
p1.say_hello()
p2.say_hello()

