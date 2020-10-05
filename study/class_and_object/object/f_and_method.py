class A:
    # 类属性，可以通过类和示例去访问
    # 只能通过类修改
    count = 0

    def __init__(self):
        # 只能通过实例对象访问
        self.name = '苏悟空'

    # 实例方法
    # 可以通过实例对象和类对象调用
    #   通过实例对象调用时，会自动传入调用对象self
    #    通过类调用时，不会自动传入self,此时必须手动传入self
    def test(self):
        print('这是一个实例方法', self)

    # 类方法
    # 在类内部使用@classmethod来修饰类方法
    # 类方法的第一个参数cls，也会被自动传递，cls是当前类对象
    #  实例对象和类对象都可以调用
    @classmethod
    def test_2(cls):
        print('这是一个类方法~~~~')
        print(cls.count)

    # 静态方法
    # 在类中使用@staticmethod来修饰的方法属于静态方法
    # 静态方法不需要任何的默认参数，可以通过类和对象去调用
    @staticmethod
    def test_3():
        print('这是一个静态方法。。。')


print(A.count)
a = A()
a.count = 10
print(a.count)
print(a.name)
A.test(a)
A.test_2()
a.test_2()
A.test_3()
a.test_3()
