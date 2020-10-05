import os
import pprint
# 文件的其他操作
r = os.listdir()

pprint.pprint(r)
print(os.getcwd())
#os.chdir('c:/')
print(os.getcwd())
# os.mkdir('aa')
# os.rmdir('aaa')
os.remove('../demo3.txt')
os.rename('../demo3.txt', '../demo4.txt')