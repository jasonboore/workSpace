stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '白骨精', '蜘蛛精']
print('原列表：', stus)

stus.append("唐僧")
print("修改后：", stus)

stus.insert(2, '猪八戒')
print("修改后：", stus)

stus.extend(['唐僧','悟空'])
print("修改后：", stus)

# stus.clear()
# print("修改后：", stus)

s = stus.pop(2)
# 删除最后一个元素
last = stus.pop()
print("修改后：", stus)
print(s)
print(last)

stus.remove('唐僧')
print("修改后：", stus)

stus.reverse()
print("修改后：", stus)

s = 'agagabnakdjfahkdf'
list = list(s)
print(list)
list.sort(reverse=True)
print(list)

list = ['Jaosn', 'Bob', 'Alice']
list.sort();
print(list)




