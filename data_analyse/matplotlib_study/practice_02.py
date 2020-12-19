import matplotlib.pyplot as plt
import random

# 1.准备数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_bejing = [random.uniform(1, 4) for i in x]

# 创建画布
# plt.figure()
figure, axes = plt.subplots(nrows=1, ncols=2)

# 绘制图像
axes[0].plot(x, y_shanghai, color='r', linestyle='-.', label='上海')
axes[1].plot(x, y_bejing, label='北京')

# 显示图例
axes[0].legend()
axes[1].legend()


# 准备x刻度说明
x_label = ['11点{}分'.format(i) for i in x]

# 处理中文字符
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 修改 x, y 刻度
# axes[0].set_xticks(x_label[::5])
axes[0].set_xticklabels(x_label[::5])
axes[0].set_yticks(range(0, 40, 5))
# axes[1].set_xticks(x_label[::5])
axes[1].set_xticklabels(x_label[::5])
axes[1].set_yticks(range(0, 40, 5))

# 设置标签
axes[0].set_xlabel('时间')
axes[0].set_ylabel('温度')
axes[0].set_title('上海市中午11-12点的温度变化')
axes[1].set_xlabel('时间')
axes[1].set_ylabel('温度')
axes[1].set_title('北京市中午11-12点的温度变化')
# 显示网格

# alpla 透明度
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[1].grid(True, linestyle='--', alpha=0.5)

# 显示图像
plt.show()
