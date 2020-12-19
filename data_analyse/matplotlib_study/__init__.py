import matplotlib.pyplot as plt

# # 画布层
# plt.figure()
# # 创建多个绘图区 / 坐标系
# # plt.subplots()
# plt.plot([1, 0, 9], [4, 5, 6])
# plt.show()

# 展示上海一周的天气
# 1.创建画布
## figsieze画布大小
## dpi图像的清晰度
plt.figure(figsize=(20, 8), dpi=80)
# 2.绘制图像
plt.plot([1, 2, 3, 4, 5, 6, 7], [17, 17, 18, 15, 11, 11, 13])

# 保存图片 不能写在plt.show()后面
plt.savefig('test78.png')
# 3.显示图像 会释放figure资源
plt.show()

