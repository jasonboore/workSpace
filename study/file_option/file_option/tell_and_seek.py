with open('../demo.txt', 'rb') as file_obj:
    # print(file_obj.read(100))
    # print(file_obj.read(30))

    # seek()可以修改当前读取的位置，单位是字节
    file_obj.seek(55)
    file_obj.seek(56)
    # seek()需要两个参数
    #   第一个 要切换的位置
    #   第二个 计算位置方式
    #     可选值：
    #       0 从头计算， 默认值
    #       1 从当前位置计算
    #       2 从最后位置计算

    print(file_obj.read(100))
    # tell()方法用来查看当前读取的位置
    print(file_obj.tell())
