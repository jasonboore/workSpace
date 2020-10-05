# 文件读取
file_name = '../demo2.txt'
# 简化版打开文件吗，关闭文件的方式
try:
    # 在with语句中可以直接使用file_obj来做文件操作
    # 此时这个文件只能在with中使用，with代码块结束，文件自动关闭
    # 文件分为两种类型
    # 1. 纯文本文件（使用utf-8等编码编写的文本文件）
    # 2. 二进制文件（图片， MP3， ppt等文件）
    # open（）默认是以文本文件的形式打开，默认编码是None
    with open(file_name, encoding='utf-8') as file_obj:
        # 如果直接调用read()它会将文本文件的所有内容读取出来
        content = file_obj.read()  # 7个字符
        print(content)

except FileNotFoundError:
    print(f'{file_name}不存在！')
