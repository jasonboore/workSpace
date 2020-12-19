print('Hello')

# try:
#    代码块（可能出现错误的代码）
# except:
#   代码块（出现错误的处理语句）
# else:
#    代码块（没出现错误时执行）
# finally；
#     代码块（无论是否出现异常都执行）

x = 1
x += 10
print(x)
try:
    print(10 / 0)
except:
    print('哈哈哈，出错了！')

print('Bye')