class Person:
    def __init__(self, name):
        self._name = name

    # @property装饰器，用来将一个get方法，转换为对象
    # 使用property装饰的方法，必须和属性名是一样的
    @property
    def name(self):
        return self._name

    # 使用 属性.setter 必须先有@property装饰的get方法
    @name.setter
    def name(self, name):
        self._name = name


p = Person('悟空')
print(p.name)
p._name = '八戒'
print(p.name)
