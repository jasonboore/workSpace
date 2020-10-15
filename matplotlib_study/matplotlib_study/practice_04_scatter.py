import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(0, 100, 50)
y = 3 * x + 1

# 创建画布
plt.figure()
# 绘制图像
plt.scatter(x, y)
# 显示图像
plt.show()