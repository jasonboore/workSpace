import numpy
import time
import random

l = []
for i in range(20000000):
    l.append(random.random())


ndarray_list = numpy.array(l)
t1 = time.time()
s1 = sum(l)
t2 = time.time()

print(t2 - t1)

t3 = time.time()
s2 = numpy.sum(ndarray_list)
t4 = time.time()

print(t4 - t3)