s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
result = s1 & s2
print(result)

result = s1 | s2
print(result)

result = s1 - s2
print(result)

result = s1 ^ s2
print(result)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
result = a <= b
print(result)

result = {1, 2, 3} <= {1, 3, 5, 6, 7}
print(result)

result = {1, 2, 3} < {1, 2, 3}
print(result)