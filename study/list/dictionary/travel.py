d = dict(name='孙悟空', age=18, gender='男')
print(d.keys())
for key in d.keys():
    print(key, ":", d[key])

for val in d.values():
    print(val)
print(d.items())

for key, val in d.items():
    print(key,'=', val)
