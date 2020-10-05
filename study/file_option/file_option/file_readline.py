file_name = '../demo2.txt'

with open(file_name, encoding='utf-8') as file_obj:
    # content = file_obj.readline()
    # print(content)

    contents = file_obj.readlines()
    for line in contents:
        print(line, end='')