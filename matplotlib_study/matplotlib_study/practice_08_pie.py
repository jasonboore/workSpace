import matplotlib.pyplot as plt

# 准备数据
movies = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记', '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其他']
place_count = [60605, 54546, 45819, 28243, 13270, 9945, 7679, 6799, 6101, 4621, 20105]
colors = ['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'b']

# 创建画布
plt.figure()

# 绘制图像
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.pie(place_count, labels=movies, colors=colors, autopct="%1.2f%%")
plt.legend()
plt.axis('equal')
# 显示图像
plt.show()