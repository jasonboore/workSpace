class Dog:
    def __init__(self, name, age, gender, height, cloth):
        self.hidden_name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.cloth = cloth

    def woof(self):
        print('%s在叫！' % self.hidden_name)

    def hit(self):
        print(f'{self.hidden_name}攻击！')

    def run(self):
        print(f'{self.hidden_name}跑！')

    def show(self):
        self.cloth.print_color()


class Cloth:
    def __init__(self, color):
        self.color = color

    def print_color(self):
        print(f'这个狗的衣服是{self.color}!')


dog1 = Dog('101', 1, '公', '15cm', Cloth('red'))
dog1.woof()
dog1.hit()
dog1.run()
dog1.show()

