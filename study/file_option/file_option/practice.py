file_name = r'C:\Users\jasonborn\Desktop\测试题目0926\测试题目0926\1-词性统计\sample-data\chinese.token.tag'
dic = dict()
with open(file_name, encoding='utf-8') as file_obj:
    contents = file_obj.readlines()
    for line in contents:
        item = line.split(r' ')
        for str in item:
            if str != '\n':
                s = str.split(r'/')[1]
                dic[s] = dic.setdefault(s, 0) + 1

for key in dic.keys():
    print(key,':', dic[key])

