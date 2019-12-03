#! /usr/bin/python3
# encoding: utf-8
"""模块shopping_cart模拟一个用户购买商品时的流程。

分为：
    加载用户账户数据结构：账号、密码；
    加载商品数据结构：商品名、商品价格；
    加载用户状态数据结构：是否第一次、已购商品；
    验证用户账户密码；
    打印商品列表：
        购买
        更新消费记录
        查询
        充值
        退出：
            打印余额
            打印消费记录
五大部分。
"""

import os
import copy

# 加载用户账户数据结构：账号、密码
try:
    user_info_list = list()
    with open('shopping_user_info.txt', mode='rt', encoding='utf-8') as fp_userinfo:
        for line in fp_userinfo:
            user_info_list.append(line.strip().split(','))
        else:
            user_info_dict = dict(user_info_list)
except FileNotFoundError as ExpFile:
    print('Type of Exceptions: {}'.format(ExpFile.__class__.__name__))
    print('Info of Exceptions: {}'.format(ExpFile))
    exit()
else:
    print('Account data loaded successfully!')

# 加载商品数据结构：商品名、商品价格
try:
    goods_list = list()
    with open('goods.txt', encoding='utf-8') as fp_goods:
        for line in fp_goods:
            tmp_list = line.strip().split(',')
            tmp_len = len(tmp_list)
            for index in range(tmp_len):
                tmp_list[index] = tmp_list[index].split(':')
            goods_list.append(dict(tmp_list))
except FileNotFoundError as ExpFile:
    print('Type of Exceptions: {}'.format(ExpFile.__class__.__name__))
    print('Info of Exceptions: {}'.format(ExpFile))
    exit()
else:
    print('Merchandise data loaded successfully!')

# 加载用户状态数据结构：是否第一次、已购商品
try:
    with open('user_status.txt', encoding='utf-8') as fp_userstatus:
        user_status_list = list()
        for line in fp_userstatus:
            tmp_dc = eval(line.strip())
            user_status_list.append(tmp_dc)
except FileNotFoundError as ExpFile:
    print('Type of Exceptions: {}'.format(ExpFile.__class__.__name__))
    print('Info of Exceptions: {}'.format(ExpFile))
    exit()
else:
    print('User status loaded successfully!')

# 验证用户账户密码
while 1:
    account = input('Input your account, please: ').strip()
    passwd = input('Input your password, please: ').strip()
    if account in user_info_dict and passwd in user_info_dict[account]:
        st_len = len(user_status_list)
        for index in range(st_len):
            key = list(user_status_list[index].keys())[0]
            if account == key:  # 如果此用户不是第一运行这个程序，那么直接取出上次的登录所剩的余额
                salary = user_status_list[index][key]['balance']
                break
        else:
            while 1:  # 表示此用户是第一次运行这个程序，请Ta输入工资
                salary = input('Input your salary(integer), please: ').strip()
                if salary.isdigit():
                    salary = int(salary)
                    break
                else:
                    print('Unacceptable salary, please Re-enter!')
        break
    else:
        print('Wrong account or password, please Re-enter!')

# 打印商品列表
# 最外层while控制商品的显示、额外功能的使用(包括买、更新、充值、查询、回退、退出)
#       买：
#          将能买的商品加入购物车并且扣除
#          更新：
#              更新用户的消费记录
#       充值：
#          当余额不足时，直接跳转到充值入口
#          按'T'自觉充值
#       查询：
#          按'S'查询 [余额，之前和现在的消费记录，返回商品列表]
#       退出：
#          按'Q'退出，保存用户消费记录于文件
# 内层while主要是为当余额不足时，询问是否直接跳转到充值接口而写
goods_list_len = len(goods_list)  # 记得向老师请教print时中文和英文排版一致
balance = salary
bought_list = []

while 1:
    for index in range(goods_list_len):  # 显示
        elm_dict = goods_list[index]
        v1, v2 = elm_dict.values()
        print('{0:4}{1:^30}{2:>6}￥'.format(index + 1, v1, v2))
    print('Press q to Quit, t to Top_up, s to search record OR')
    seq_num = input('Enter the sequence number you want to buy: ').strip()
    while 1:
        if seq_num.isdigit():  # 买
            seq_num = int(seq_num) - 1
            if seq_num < goods_list_len:
                price = float(goods_list[seq_num]['price'])
                if balance >= price:
                    balance = balance - price
                    for index in range(len(bought_list)):  # 更新已买商品
                        dc = bought_list[index]
                        if goods_list[seq_num]['name'] == dc['name']:
                            dic['amount'] = dic.setdefault('amount', 0) + 1
                            break
                    else:
                        dic = copy.deepcopy(goods_list[seq_num])
                        dic['amount'] = dic.setdefault('amount', 0) + 1
                        bought_list.append(dic)
                    print('You now have bought [x{} {}'.
                          format(dic['amount'], goods_list[seq_num]['name']))
                    print('You have {}￥ left'.format(balance))
                    break
                else:  # 余额不足，询问是否充值
                    print('Sorry! Your balance is NOT enought.')
                    print('Do you want to recharge?(yes/no) ', end='')
                    response = input().strip()
                    if response.upper() == 'YES' or not response:
                        seq_num = 't'
                        continue
                    else:
                        break
        elif seq_num.upper() == 'Q':  # 退出
            flag = False  # 标志用户是否是第一次登陆，False不是，True是
            bought_len = len(bought_list)
            print('So far, you have bought: ')
            if not bought_len:
                print('Nothing!')
            else:
                for index in range(bought_len):  # 打印这次登录所买的商品信息
                    print('{name:30}{price:>10}￥\t\tx{amount:}'.format_map(bought_list[index]))
                else:
                    print('You have {}￥ left'.format(balance))
                    print('Hope to see you again!')
            for index in range(len(user_status_list)):  # 判断是否为新用户。是，直接构造数据结构并且写入；不是，延用上次的
                st_dc = user_status_list[index]
                key = list(st_dc.keys())[0]
                if account in key:
                    break
            else:
                flag = True
            if flag:  # 为新用户构造数据结构
                define_dc = dict()
                define_dc[account] = {'balance': balance, 'record': bought_list}
                user_status_list.append(define_dc)
            else:  # 老用户更新数据结构
                for index in range(len(user_status_list)):
                    st_dc = user_status_list[index]
                    key = list(st_dc.keys())[0]
                    updated_list = st_dc[key]['record']
                    if account == key:
                        st_dc[key]['balance'] = balance
                        for index in range(len(bought_list)):  # 用这次买的商品列表更新之前买的商品列表
                            bt_dc = bought_list[index]
                            for index in range(len(updated_list)):
                                if bt_dc['name'] == updated_list[index]['name']:
                                    updated_list[index]['amount'] += bt_dc['amount']
                                    break
                            else:
                                updated_list.append(copy.deepcopy(bt_dc))
            # print(len(user_status_list))
            with open('user_status_ectype.txt', mode='w', encoding='utf-8') as fp_userstatus:
                for line in user_status_list:
                    fp_userstatus.write(str(line) + '\n')
            os.remove('user_status.txt')
            os.replace('user_status_ectype.txt', 'user_status.txt')
            exit()
        elif seq_num.upper() == 'T':  # 充值
            money = input('Enter the money(integer) you want to top-up: ')
            money = money.strip()
            balance += int(money)
            print('Updated successfuly, your balance is {}￥'.format(balance))
            break
        elif seq_num.upper() == 'S':  # 查询
            while 1:
                print('Press b to search balance, r to search record, OR e to return list: ', end='')
                code = input().strip()
                if code.upper() == 'B':
                    print('You have {}￥ left'.format(balance))
                elif code.upper() == 'R':
                    print('<-------------- the past record -------------->')
                    for index in range(len(user_status_list)):
                        st_dc = user_status_list[index]
                        key = list(st_dc.keys())[0]
                        recorded_list = st_dc[key]['record']
                        if account == key:
                            reco_len = recorded_list.__len__()
                            for index in range(reco_len):
                                dc = recorded_list[index]
                                print('{name:<30}{price:>7}￥\t\tx{amount}'.format_map(dc))
                        break
                    print('<-------------- the past end -------------->\n')

                    print('<-------------- the recent record -------------->')
                    for index in range(len(bought_list)):
                        bt_dc = bought_list[index]
                        print('{name:<30}{price:>7}￥\t\tx{amount}'.format_map(bt_dc))
                    print('<-------------- the recent end -------------->\n')
                elif code.upper() == 'E':
                    break
            break
        else:
            print('Invalid sequence number, please Re-enter!')
            break
