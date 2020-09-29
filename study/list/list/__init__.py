my_friend = ['Bob', 'Jason', 'David', 'Tom', 'Google','Jason', 'Jason']
for i in range(0, len(my_friend)):
    print(str(i) + ' ' + my_friend[-i])

print(my_friend[-3:])
print(my_friend[1:5])
print(my_friend[:3])

#复制列表
print(my_friend[:])
print(my_friend[::-1])

my_list = [1,2,3] + [4,5,6]
print(my_list)

arr = [0] * 20
print(arr)

print('Bob' in my_friend)
print('Alice' in my_friend)
print('Alice' not in my_friend)

print(min(my_list))
print(max(my_friend))
print(min(my_list), max(my_list))

s = 'hello world'
print('h' in s)

print(my_friend.index('Jason', 1))#从第一个开始找
print(my_friend.count('Jason'))
print(my_friend.count('Alice'))

