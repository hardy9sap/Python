"""
升级需求：
可以支持多个用户登录 (提示，通过列表存多个账户信息)
用户3次认证失败后，退出程序，
再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）
"""

import os

# 加载用户信息, 创建包含用户账户、密码、状态的字典
with open('user_info.txt', mode='r', encoding='utf-8') as fp:
    user_info_list = list()
    for line in fp:
        tmp_list = line.strip().split(maxsplit=1)
        tmp_list[-1] = tmp_list[-1].split()
        # tmp_tuple = tuple(tmp_list)
        user_info_list.append(tmp_list)
    else:
        user_info_dict = dict(user_info_list)
# print(user_info_dict)

# 格式化字符串
outer_chance = inside_chance = 'chances'
still_chance = '\033[30mYou still have \033[1;31m%d %s\033[0m \033[30mto log in.\033[0m'
now_chance = '\033[30mYou now have \033[1;31m%d %s\033[0m \033[30mto log in.\033[0m'
acc_formatter = 'Enter your account: '
pass_formatter = 'Enter your passcode: '
invalid_formatter = '\033[31mInvalid account. Please Re-enter!\033[0m'
no_chance_formatter = '\033[1;31mYou have no chance. Bye now!\033[0m'
locked_formatter = 'Your account has been \033[1;31mlocked down\033[0m. Please try again later!'
login_formatter = '\033[1;34mLog in successfully!\033[0m'
login_failed_formatter = '\033[1;34mLog in failed!\033[0m'

# 尝试登陆
chances = 3  # 3次登录机会
is_same_account = True  # 表明是三次输入的账号都是同一个
previous_account = None
while chances:  # 最外层while验证账号
    if chances == 3:
        print(now_chance % (chances, outer_chance))  # 一运行就打印你有3次机会
        account = input(acc_formatter).strip()  # 输入账号
    elif chances < 3:
        if chances == 1:  # 'chance'变为单数
            outer_chance = outer_chance[0:-1]
        print(still_chance % (chances, outer_chance))
        account = input(acc_formatter).strip()  # 输入账号
    if previous_account is None:
        previous_account = account
    if previous_account != account:
        is_same_account = False
    if account in user_info_dict:  # 判断账号是否在字典中。若不在，则重新输入，并且次数减一
        user_status = eval(user_info_dict[account][-1])
        if not user_status:  # 判断账户的状态，是否为锁定
            while chances:  # 这层while验证账号对应的密码是否正确
                passcode = input(pass_formatter).strip()
                if passcode in user_info_dict[account][0]:
                    print(login_formatter)
                    break
                else:
                    chances -= 1  # chances - 1
                    if 0 < chances < 3:
                        if chances == 1:
                            inside_chance = inside_chance[0:-1]
                        print(login_failed_formatter)
                        print(still_chance % (chances, inside_chance))
                    pass
            else:  # 三次登录失败，将用户信息写入文件
                if is_same_account:
                    user_info_dict[account][-1] = str(not user_status)  # 更改登录状态
                    with open('user_info_ectype.txt', mode='w', encoding='utf-8') as fp:
                        length = len(user_info_list)
                        for index in range(length):  # 将列表的每一个为列表的元素转成字符串
                            tmp_list = user_info_list[index]
                            tmp_len = len(tmp_list)
                            for sub_index in range(tmp_len):  # 将类型为列表的元素里面的列表元素转成字符串
                                elm = tmp_list[sub_index]
                                if type(elm) is list:
                                    tmp_list[sub_index] = ' '.join(elm)
                            user_info_list[index] = ' '.join(tmp_list) + '\n'  # 为每个用户增加一个换行符
                        fp.writelines(user_info_list)
                    os.remove('user_info.txt')
                    os.rename('user_info_ectype.txt', 'user_info.txt')
                    # print(no_chance_formatter)
                print(login_failed_formatter)
                print(no_chance_formatter)
            exit()
        else:
            print(login_failed_formatter)
            print(locked_formatter)
            exit()
    else:
        print(invalid_formatter)
        chances -= 1
else:
    print(no_chance_formatter)
    exit()

