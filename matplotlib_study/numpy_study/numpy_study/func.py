import numpy
import matplotlib.pyplot as plt

# 生成 0和1的数组
zeros = numpy.zeros([3, 4], dtype=numpy.float32)
print(zeros)

ones = numpy.ones([2,3], dtype=numpy.int64)
print(ones)

score = numpy.array([[80, 89, 86, 67, 79],
                     [78, 97, 89, 67, 81],
                     [90, 94, 78, 67, 74],
                     [91, 91, 90, 67, 69],
                     [76, 87, 75, 97, 86],
                     [70, 79, 84, 67, 84],
                     [94, 92, 93, 67, 64],
                     [86, 85, 83, 67, 80]], dtype=numpy.int64)

print(score)
# 深拷贝  对原始数组操作不影响其数组
data1 = numpy.array(score)
print(data1)
# 浅拷贝
data2 = numpy.asarray(score)
print(data2)
# 深拷贝  对原始数组操作不影响其数组
data3 = numpy.copy(score)
print(data3)

score[0, 0] = 100
print('score', score)
print('data1', data1)
print('data2',data2)
print('data3',data3)

# 生成固定长度的数组
# 范围[0, 10]等距离生成100个数
lin_list = numpy.linspace(0, 10, 100)
print(lin_list)
# [a, b]范围，c是步长
# ran_list = numpy.arange(a, b ,c)
ran_list = numpy.arange(0, 10, 0.5)
print(ran_list)


#生成随机数组
random_list = numpy.random.uniform(low=-1, high=1, size=1000000)
print(random_list)
# 均匀分布
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(random_list, 1000)
plt.show()

# 正态分布
# loc 均值
# scale标准差
data2 = numpy.random.normal(loc=1.75, scale=0.1, size=1000000)
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(data2, 1000)
plt.show()


