"""
作业需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序
"""
user_info_dict = {'username': 'QinDongyu',
                  'password': '123'
                  }  # 创建用户账户和密码字典
chance = 'chances'  # 单词'chance'单复数
count = 3  # 3次登录机会
print('You now have %d %s to log in.' % (count, chance))
while count:  # 为0就停止循环
    if count < 3:
        if count == 1:  # 'chance'变为单数
            chance = chance[0:-1]
        print('You still have %d %s to log in.' % (count, chance))
    username = input('Enter your account: ').strip()
    password = input('Enter your password: ').strip()
    if (username == user_info_dict['username'] and
            password == user_info_dict['password']):
        print('Log in successfully!')
        break
    else:
        count -= 1  # 登录失败count - 1
else:
    print('You have no chance!')
    exit()
