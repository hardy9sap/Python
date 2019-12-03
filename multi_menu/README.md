# <center>说明文档目录</center>

1. 开发环境
2. 功能实现
3. 启动方式
4. 登录用户信息
5. 程序运行效果
6. 常见问题


# 开发环境
    Windows 8(64位)
    Python(3.7.0)
    JetBrains PyCharm(2018.2.2 x64)


# 功能实现
    在有多个层级的菜单中来回切换
    1. 可依次选择进入各子菜单
    2. 可从任意一层往回退到上一层
    3. 可从任意一层退出程序


# 启动方式
    脚本执行
        1. CMD终端下   python3 multi_menu.py
           PS: 如果系统中安装了python2，则按照上行方式执行；
               如果没有，则执行 python multi_memu.py
               
        2. PyCharm下   打开文件后，鼠标右键单击执行"Run 'multi_memu'"或按快捷键ctrl + shift + F10
        
        3. IDLE下      打开文件后，按F5


# 登录用户信息
    无

# 程序运行效果
1. CMD终端下

![cmd][]

2. PyCharm下
![pycharm][]

3. IDLE下
![idle][]

# 常见问题
## 问题
**CMD终端下报No such file or directory**
![error][]

## 解决
检查你当前所在目录是否有`multi_memu.py`此文件



   [cmd]: "https://note.youdao.com/yws/public/resource/11390fbe9383929872189d62f8df78c5/xmlnote/41961E7B20CF4432BB0FA912E6D12F9C/176"

   [pycharm]: "https://note.youdao.com/yws/public/resource/11390fbe9383929872189d62f8df78c5/xmlnote/38B0679052354505A6B1729B443622C5/178"

   [idle]: "https://note.youdao.com/yws/public/resource/11390fbe9383929872189d62f8df78c5/xmlnote/7F485137FFBD497C817D7B69A8161A2D/182"

   [error]: "https://note.youdao.com/yws/public/resource/11390fbe9383929872189d62f8df78c5/xmlnote/C836A212564948FFA701A9F5692DFC70/184"