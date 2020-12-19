import numpy

grades = [[80, 86], [82, 80], [85, 78], [90, 90], [86, 82], [82, 90], [78, 80], [92, 94]]
data_arr = numpy.array(grades)
data_mat = numpy.mat(grades)
print(data_mat, type(data_mat))

# 矩阵乘法运算
## 要求：形状  (m * n) * (n * l)

weight = numpy.array([[0.3], [0.7]])
# 不满足广播机制，不能运算
result = data_arr * weight
print(result)

# 矩阵乘法api
## numpy.matmul
## numpy.dot

print('numpy.matmul',numpy.matmul(data_arr, weight))
print('numpy.dot', numpy.dot(data_arr, weight))
print(data_arr @ weight)
