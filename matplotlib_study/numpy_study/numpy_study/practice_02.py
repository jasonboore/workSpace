import numpy

stock_change = numpy.random.normal(loc=0, scale=1, size=(8, 10))
# 逻辑判断，如果涨幅大于0.5， 就标记为True,否则标记为False
mark = stock_change > 0.5
print(mark)
# 逻辑索引
print(stock_change[stock_change > 0.5])

#通用判断函数
# numpy.all(布尔值)
## 如果有一个False 则返回False, 全为True，则返回True
# numpy.any(布尔值)
## 如果有一个True则返回True， 全为False，则返回False
print(numpy.all(stock_change[0:2, 0:5] > 0))
print(stock_change[0:1])
print(stock_change[0:1, :])
print(numpy.any(stock_change[0:5, :]> 0))

# numpy.where(布尔值, True的位置的值, False的位置的值)
temp = stock_change[0:4]
print(temp)
print(numpy.where(temp > 0, 1, 0))

print(numpy.where(numpy.logical_and(temp > 0.5, temp < 1), 1, 0))
print(numpy.where(numpy.logical_or(temp > 0.5, temp < -0.5), 1, 0))

# 前四只股票的最大涨幅
print(temp.max(axis=1))
print(numpy.max(temp, axis=1))

print(numpy.argmax(temp, axis=1))



