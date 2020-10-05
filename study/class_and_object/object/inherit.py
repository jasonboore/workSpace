class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def run(self):
        print('跑！')

    def jump(self):
        print('跳')

    @staticmethod
    def eat(self):
        print('吃！')


# 类中所有方法都会被继承，包括特殊方法

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

#    方法重写

    def run(self):
        print('狗跑！')


d = Dog('旺财', 18)
d.run()
print(d.name)
print(d.age)
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(issubclass(Dog, Animal))
print('---------')

