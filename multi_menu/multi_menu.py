#! /usr/bin/python3
r"""模块multi_memu是用于在有多个层级的菜单中来回切换。

Raises:
    IndexError: Sequence index out of range.
"""


menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

current_layer = menu  # 设置当前层
layer_list = list()  # 存放上一层
while 1:
    for layer in current_layer:
        print(layer)
    city = input('Please enter a city(q to quit, b to back): ').strip()
    if city.upper() == 'Q':
        print('Thank you for your use. Please call again.')
        break
    elif city.upper() == 'B':
        if not layer_list:
            print('You\'re already on top!')
        else:
            current_layer = layer_list.pop()  # 取出上一层，并删除
    else:
        if city in current_layer:
            layer_list.append(current_layer)  # 将当前层加入到列表
            current_layer = current_layer[city]  # 重新定义当前层，当前层的下一层
        else:
            print('Sorry, your inputs are out of the operating range.')