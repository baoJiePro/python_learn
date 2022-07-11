# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/9 15:42

# ### 闭包函数
"""
内函数使用了外函数的局部变量,
并且外函数把内函数返回出来的过程叫做闭包
这个内函数叫做闭包函数

# 闭包函数的语法:
def outer():
	a = 5
	def inner():
		print(a)
	return inner

# 对比正常的局部变量
# 局部变量的生命周期最短,在调用结束之后,立即释放.
def func():
	a = 5
	print(a)
func()
print(a)

"""


# (1) 闭包函数的定义
def h_family():
    father = "王健林"

    def h_say():
        print("我老爸%s说了,先定一个小目标,比如赚他一个亿" % father)

    return h_say


func = h_family()
func()

h_family()()

# (2) 闭包函数的特点(升级)
'''
闭包的特点:
    内函数使用了外函数的局部变量,外函数的局部变量与内函数发生绑定,延长该变量的生命周期
    (实际内存给它存储了这个值,暂时不释放)
'''


def l_family():
    jiejie = "马蓉"
    meimei = "马诺"
    money = 1000

    def j_hobby():
        nonlocal money
        money -= 600
        print("姐姐%s喜欢花钱,买名牌包包,手表,彩电,冰箱,电脑,洗衣机,热水器,家里的钱还剩下%s" % (jiejie, money))
        return money

    def m_hobby():
        nonlocal money
        money -= 300
        print("妹妹%s喜欢花钱,买LV,香奈儿,倩碧,雅诗兰黛,大宝,六神花露水,肥皂,雕牌洗衣粉,洗涤剂,家里的钱还剩下%s" % (meimei, money))
        return money

    def big_manager():
        return j_hobby, m_hobby

    return big_manager

func = l_family()
tup = func()
print(tup, type(tup))

res = tup[0]()
print(res)

res = tup[1]()
print(res)


def outer(val):
    def inner(num):
        return val + num

    return inner

func = outer(10)
# func = inner
res = func(5)
print(res)
# 获取闭包函数使用的绑定变量 闭包函数.__closure__  返回单元cell  , cell 里面存的是对应的绑定变量
res = func.__closure__
print(res, type(res))
# res[0] 获取元组当中的第一个值 是一个cell单元 通过单元.cell_contents来获取其中的值,就会知道绑定的变量是谁了. cell_contents是一个属性
res = res[0].cell_contents
print(res)
"""
# 代码解析:
	func = outer(10)
	val 形参接收到实参值10
	因为内函数使用了外函数的局部变量val,val与内函数发生绑定,延长val的生命周期
	res = func(5)
	num 形参接收到实参值5
	return 10 + 5 => return 15 返回到函数的调用处
	func(5) 是调用处 所以
	res = 15
"""

def click():
    x = 0
    def func():
        nonlocal x
        x += 1
        return x
    return func

click = click()
res = click()
res = click()
print(res)



