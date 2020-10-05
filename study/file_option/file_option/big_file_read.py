# 大文件读取
file_name = '../demo.txt'
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
        # 如果要读取的文件较大的话，会一次性将文件内容全部加载到内存中，出现问题
        # 所以较大的文件不能直接用read()
        # read()可以直接接收一个size作为参数，该参数用来指定要读取的字符的数量
        # 默认值为-1，它会读取文件中所有的字符,单位是字符
        # 每一次读取从上一次读到的位置开始读取
        # 如果已经读取到最后了，则会返回一个空串

        content = file_obj.read(7)  # 7个字符
        while content:
            print(content, end='')
            # print(len(content))
            content = file_obj.read(7)  # 7个字符

except FileNotFoundError:
    print(f'{file_name}不存在！')
