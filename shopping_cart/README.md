# <center>说明文档目录</center>
1. 开发环境
2. 功能实现
3. 启动方式
4. 登录用户信息
5. 程序运行效果
6. 常见问题


# 开发环境
    Windows 10(64位)
    Python(3.7.0)
    JetBrains PyCharm(2018.2.2 x64)

# 功能实现
	1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
	2、允许用户根据商品编号购买商品
	3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
	4、可随时退出，退出时，打印已购买商品和余额
	5、在用户使用过程中，关键输出，如余额，商品已加入购物车等消息，进行高亮显示
	6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
	7、允许查询之前的消费记录  


# 启动方式
    脚本执行
        1. CMD终端下   python3 shopping_cart_nocolor.py
           PS: 如果系统中安装了python2，则按照上行方式执行；
               如果没有，则执行 python shopping_cart_nocolor.py
               
        2. PyCharm下   打开文件后，鼠标右键单击执行"Run 'shopping_cart'"
		   或按快捷键ctrl + shift + F10
        
        3. IDLE下      打开shopping_cart_nocolor.py后，按F5



# 登录用户信息
    来自于shopping_user_info.txt文件


# 程序运行效果
1. CMD终端下
![cmd][]
2. PyCharm下
![pycharm][]
3. IDLE下
![idle][] 



   [cmd]: "https://note.youdao.com/yws/public/resource/068eb5e3f1ecaf7eaba1670da1067fc2/xmlnote/1123E0D32B2D4AF09D1D660981FFA6CB/189"

   [pycharm]: "https://note.youdao.com/yws/public/resource/068eb5e3f1ecaf7eaba1670da1067fc2/xmlnote/7965C7E291E348C69DFA16013DB547D1/192"

   [idle]: "https://note.youdao.com/yws/public/resource/068eb5e3f1ecaf7eaba1670da1067fc2/xmlnote/28C2B7DD7B7140DFA70F292068D53D7E/194"



# 常见问题
## 问题
`File not found.`
## 解决
    确保shopping_cart.py / shopping_cart_nocolor.py和goods.txt、user_status.txt、shopping_user_info.txt在同一目录下
    如果文件缺失，请联系我hardy9sap@163.com
