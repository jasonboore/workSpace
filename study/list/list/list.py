stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '白骨精', '蜘蛛精']
del stus[2]

# 0位置插入元素
stus[0:0] = ['牛魔王']
print(stus)

stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '白骨精', '蜘蛛精']
stus[0:2] = 'swk'
print(stus)
# 当设置步长时，序列中元素的个数必须和切片中元素的个数一致
stus[::2] = ['1','2','3','4']
print(stus)
del stus[::2]
stus[0:1] = []
print(stus)

s = 'hello'
s = list(s)
print(s)