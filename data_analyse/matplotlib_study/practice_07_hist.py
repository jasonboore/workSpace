import matplotlib.pyplot as plt

# 准备数据
time = []
# 创建画布
plt.figure()
# 绘制图像
## x = 横坐标
## bins = 组数 = int(max(x) - min(x) // 组距)
# y轴变量可以是频数也可以是频率
distance = 2
group_num = int((max(time) - min(time)) / distance)
plt.hist(time, bins=group_num)
plt.xticks(range(min(time), max(time), distance))
# 显示图像
plt.show()