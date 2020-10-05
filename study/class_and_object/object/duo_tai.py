# 多态度

class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class C:
    pass

def say_hello(obj):
    print('你好啊，%s'%obj.name)

def say_hello2(obj):
    if isinstance(obj, A):
        print('你好啊，%s' % obj.name)

a = A('孙悟空')
b = B('猪八戒')
c = C()
say_hello(a)
say_hello2(a)
# 之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
# 换句话说，只要对象中具有__len__特殊方法，就可以通过len()来获取他的长度
print(len(b))