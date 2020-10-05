dic = dict()
contents = '新华社/NR 乌鲁木齐/NR $date/JJ 电/NN (/NN 记者/NN 樊/NR 英/NR 利/NN ,/PU 丁/VV 建刚/NR ,/PU 李秀/NR 芩/VV )/NN 为/P 促进/VV 民族团结/NN ,/PU 维护/VV 社会/NN 安定/VA ,/PU 近年来/NT 新疆/NR 伊犁/NR 创造性/NN 地/DEV 开展/VV 了/AS "/JJ 面对面/JJ "/NN 宣讲/NN 活动/NN ,/PU 让/VV 各族/NN 群众/NN 听到/VV 了/AS 党/NN 和/CC 政府/NN 的/DEG 声音/NN ,/AD 受到/VV 热烈欢迎/NN ./PU'
contents.replace('\n', '')

item = contents.split(r' ')
print(item)
print('------------')
for str in item:
    if str :
        s = str.split(r'/')[1]
        print(s)
        dic[s] = dic.setdefault(s, 0) + 1

for key in dic.keys():
    print(dic[key])