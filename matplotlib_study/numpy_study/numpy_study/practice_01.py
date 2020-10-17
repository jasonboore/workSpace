import numpy

stock_change = numpy.random.normal(loc=0, scale=1, size=(8, 10))
print(stock_change[0, :3])

a = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 34], [4, 5, 6]]])
print(a[1, 0, 1:])

print(stock_change)
# 返回新的ndarray，但是原始数据没有改
print(stock_change.reshape(10, 8))
# 没有返回值，对原始的ndarray进行了修改
stock_change.resize(10, 8)
print(stock_change.shape)
stock_change.resize(8, 10)


# 转置
print(stock_change.T)

reType = stock_change.astype('int32')
print(reType, reType.dtype)
print(reType.tostring())

print(numpy.unique(a))

