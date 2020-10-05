# 1. 打开文件
# 2. 操作文件（读/写）
# 3. 关闭文件


# 绝对路径
file_name = 'C:/Users/jasonborn/Desktop/命名表.xlsx'
#  使用原始字符串
file_name = r'C:\Users\jasonborn\Desktop\命名表.xlsx'

# 相对路径
file_name = '../demo.txt'

# 打开相应的文件
file_obj = open(file_name)

content = file_obj.read()

print(content)

file_obj.close()


