import numpy

score = numpy.array([[80, 89, 86, 67, 79],
                     [78, 97, 89, 67, 81],
                     [90, 94, 78, 67, 74],
                     [91, 91, 90, 67, 69],
                     [76, 87, 75, 97, 86],
                     [70, 79, 84, 67, 84],
                     [94, 92, 93, 67, 64],
                     [86, 85, 83, 67, 80]], dtype=numpy.int64)

print(score)
# ndarray 属性
print(score.shape)
print(score.ndim)
print(score.size)
print(score.dtype)
print(score.itemsize)

# shape元素中几个数就是几维数组
npList = numpy.array([1, 2, 3])
print(npList.shape)
print(npList.ndim)

npList = numpy.array([[1, 2, 3], [4, 5, 6]])
print(npList.shape)
print(npList.ndim)

npList = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(npList.shape)
print(npList.ndim)