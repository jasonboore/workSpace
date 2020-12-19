import matplotlib.pyplot as plt

movies = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记', '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其他']
tickets = [73853, 57767, 22354, 15969, 14839, 8725, 8716, 8318, 7916, 6764, 52222]
colors = ['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'b']
# 创建画布
plt.figure()
# 绘制图像
x_ticks = range(len(movies))
plt.xticks(x_ticks, movies, rotation=90)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.bar(x_ticks, tickets, color=colors)
plt.title('电影票房收入对比')
plt.grid(True, linestyle='--', alpha=0.5)
# 显示图像
plt.show()
