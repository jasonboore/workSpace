import matplotlib.pyplot as plt
import numpy

# 准备数据
x = numpy.linspace(-10, 10, 1000)
y = 2 * x * x
# 创建画布
plt.figure()
# 绘制图像
plt.plot(x, y)
plt.grid(True, linestyle='--')
# 显示图像
plt.show()