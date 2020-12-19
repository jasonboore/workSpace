import matplotlib.pyplot as plt

movie_names = ['雷神3：诸神黄昏', '正义联盟','寻梦环游记']
first_day = [10587.6, 10062.5, 1275.7]
first_weekend = [36224.9, 34479.6, 11830]
plt.figure()
plt.bar(range(3), first_day, width=0.2)
plt.bar([i + 0.2 for i in range(3)], first_weekend, width=0.2)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.xticks([i + 0.1 for i in range(3)], movie_names)
plt.show()
