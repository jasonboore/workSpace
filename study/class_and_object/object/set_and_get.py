# 类的封装
class Cat:
    def __init__(self, name, age, gender, weight):
        self.hidden_name = name
        self.hidden_age = age
        # 隐藏属性，不建议使用
        self.__gender = gender
        # 一般私有属性用_开头
        self._weight = weight

    def set_name(self, name):
        self.hidden_name = name

    def get_name(self):
        return self.hidden_name

    def setAge(self, age):
        if age > 0:
            self.hidden_age = age

    def getAge(self):
        return self.hidden_age

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender


c = Cat('咪咪', 2)
print(c.get_name())
print(c.getAge())

c.set_name('小小')
c.setAge(8)
print(c.get_name())
print(c.getAge())

