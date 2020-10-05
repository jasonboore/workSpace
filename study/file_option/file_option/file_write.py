# 文件的写入
file_name = '../demo.txt'

# w 是可写的，使用 w 写入文件时，如果文件不存在会创建文件，如果文件存在
# 会将原来文件的全部内容删除，并写入数据，w 操作只能写入字符串
# a 表示追加内容，如果文件不存在会创建文件，如果文件存在，向文件追加内容
# x 用来新建文件，如果文件不存在则创建文件，存在则报错
# + 为操作符追加内容
# r+ 既可读，又可写
# w+ 在写的基础上增加可读功能
# a+ 在追加的基础上可读
with open(file_name, 'w', encoding='utf-8') as file_obj:
    file_obj.write('Hello File!')

with open(file_name, 'a', encoding='utf-8') as file_obj:
    file_obj.write('append!')