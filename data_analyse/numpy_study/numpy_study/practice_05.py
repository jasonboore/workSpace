import numpy

# 数组拼接
# 水平拼接
a = numpy.array([1, 2, 3])
b = numpy.array([4, 5, 6])
temp = numpy.hstack((a, b))
print(temp)

a = numpy.array([[1], [2], [3]])
b = numpy.array([[2], [3], [4]])
temp = numpy.hstack((a, b))
print(temp)

# 竖直拼接
temp = numpy.vstack((a, b))
print(temp)

a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[5, 6]])
temp = numpy.concatenate((a, b), axis=0)
print(temp)

temp = numpy.concatenate((a, b.T), axis=1)
print(temp)

stock_change = numpy.random.normal(loc=0, scale=1, size=(8, 10))
a = stock_change[:2, 0:4]
b = stock_change[4:6, 0:4]
temp = numpy.hstack((a, b))
print(temp)

temp = numpy.concatenate((a, b), axis=1)
print(temp)

# 数组分割
x = numpy.arange(9)
temp = numpy.split(x, 3)
print(temp)

temp = numpy.split(x, [3, 5, 6, 9])
print(temp)

# 提取某一列
x = [[1, 2, 3],
     [4, 5, 6]]

data = numpy.array(x)
first_col = data[:, 0]
print(first_col)
