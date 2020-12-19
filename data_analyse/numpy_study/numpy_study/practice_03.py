import numpy


arr1 = numpy.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])
# 数组运算
print(arr1 / 10)

arr2 = numpy.array([[3], [1]])


# 当操作两个数组(ndarray)时，numpy会逐个比较它们的shape(构成的元组tuple),只有在下述情况下，两个数组才能够进行数组与数组的运算
## 维度相等
## shape(其中相对应的一个地方为1)
## 可以进行运算
### A       (4d array):9 * 1 * 7 * 1
### B       (3d array):    8 * 1 * 5
### Result  (3d array):9 * 8 * 7 * 5

## 不可以进行运算
### A       (4d array):9
### B       (3d array):8
### Result  (3d array):?
arr1 = numpy.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])
arr2 = numpy.array([[3], [1]])
print(arr1 + arr2)

