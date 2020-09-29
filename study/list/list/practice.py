print('-' * 20 + '欢迎使用员工管理系统' + '-' * 20)
employee = ['\t孙悟空\t18\t男\t花果山']
while True:
    print('请选择要做的操作')
    print('\t1、查询员工')
    print('\t2、添加员工')
    print('\t3、删除员工')
    print('\t4、退出系统')
    user_choose = input('请选择1-4：')
    print(user_choose)
    print('-' * 62)
    if user_choose == '1':
        print('\t序号\t姓名\t年龄\t性别\t住址')
        for i in range(0, len(employee)):
            print(f'\t{i + 1}{employee[i]}')
    elif user_choose == '2':
        emp_name = input('请输入员工姓名：')
        emp_age = input('请输入员工年龄：')
        emp_gender = input('请输入员工性别：')
        emp_addr = input('请输入员工地址：')
        emq = f'\t{emp_name}\t{emp_age}\t{emp_gender}\t{emp_addr}'
        print('请确认要添加的员工信息：')
        print('-' * 62)
        print('\t姓名\t年龄\t性别\t住址')
        print(emq)
        print('-' * 62)
        user_confirm = input('是否确认添加该员工[y/n]:')
        if user_confirm == 'y' or user_confirm == 'yes' :
            employee.append(emq)
            print('添加成功！')
        else :
            print('插入已取消！')
    elif user_choose == '3':
        del_num = int(input('请输入要删除的员工序号：'))
        if 0 < del_num <= len(employee) :
            del_index = del_num - 1
            print('请确认要删除的员工信息：')
            print('-' * 62)
            print('\t姓名\t年龄\t性别\t住址')
            print(emq)
            print('-' * 62)
            user_confirm = input('该操作不可恢复，是否确认删除[y/n]:')
            if user_confirm == 'y' or user_confirm == 'yes' :
                employee.pop(del_index)
                print('删除成功!')
            else :
                print('删除操作已取消！')
    elif user_choose == '4':
        print('欢迎使用，再见！')
        break
    else:
        print('请输入正确的数字！')
    print('-' * 62)