d = {}
print(d, type(d))

d = {
    'name': '孙悟空',
    'age': 18,
    'gender': '男',
}
print(d, type(d))
print(d['name'])
print(d['age'])
print(d['gender'])
print(d.__contains__(1))
