import re

# Y+ 对前面进行一次或无限多次扩展
# .表示任何单个字符
# *对前面的字符进行0个或无限多次扩展
# ？对前面的字符进行0次或一次扩展
# |左右表达式任选一个
# {m}扩展前一个字符m次
# {m, n}扩展前一个字符m到n次
# ^    ^abc表示abc且在一个字符串的开头
# $    abc$表示abc且在一个字符串的结尾
# () 分组标记，且只能在其中用 |
# \d 数字，等价于[0-9]
# \w 单词字符，等价于[A-Za-z0-9_]
match = re.search(r'[1-9]\d{5}', 'BIT 163000')
if match:
    print(match.group(0))

match = re.match(r'[1-9]\d{5}', '163000 BIT')
if match:
    print(match.group(0))

ls = re.findall(r'[1-9]\d{5}', '163000BIT TSU100081')
print(ls)

ls = re.split(r'[1-9]\d{5}', 'BIT163000 TSU100081')
print(ls)
match = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT163000 TSU100081')
print(match)

match = re.search('PY.*N', 'PYANBNCNDN')
print(match.group(0))
# 最小匹配
match = re.search('PY.*?N', 'PYANBNCNDN')
print(match.group(0))
