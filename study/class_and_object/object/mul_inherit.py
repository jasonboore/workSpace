# 多重继承
class A:
    def test(self):
        print('AAA')


class B:
    def test(self):
        print('BBB')

class C(A, B):
    pass





print(C().test())
print(C.__bases__)