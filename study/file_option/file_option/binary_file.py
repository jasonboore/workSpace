file_name = r'C:\Users\jasonborn\Desktop\文件夹\3D_Work\Untitled.bmp'

# 读取模式， mode
# t 读取文本文件（默认值）  以读为例：默认值 rt
# b 读取二进制文件
with open(file_name, 'rb') as file_obj:
    # 读取文本文件时，size以字符为单位
    # 读取二进制文件时，size以字节为单位
    # print(file_obj.read(100))
    # 将读取的内容写回
    new_name = 'aa.bmp'
    with open(new_name, 'wb') as new_obj:
        while True:
            chunk = 1024 * 100
            content = file_obj.read(chunk)
            if not content:
                break
            new_obj.write(content)