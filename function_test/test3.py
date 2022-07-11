# ### 收集参数
"""
(1) 普通收集参数
(2) 关键字收集参数
"""

# (1) 普通收集参数 (任意长度都可以接收)
'''
def func(*args):
	pass
*args 就是普通收集参数 : * + 参数名字(名字自定义,一般约定俗成叫做args => arguments 参数的意思)

用途:专门用于收集多余的没人要的普通实参,都放到一个元组当中收集
'''


def func(a, b, c, *args):
    print(a, b, c)
    print(args)


func(1, 2, 3, 4, 5, 33, 44, 55)


def my_sum(*args):
    total = 0
    for i in args:
        total += i
    print(total)


my_sum(1, 2, 3, 5, 6)

# 关键字收集参数
'''
def func(**kwargs):
	pass
**kwargs 就是关键字收集参数 : ** + 参数名字 (名字自定义,一般约定俗成叫做kwargs => keyword arguments 参数的意思)	

用途:专门用于收集多余的没人要的关键字实参,都放到一个字典当中收集	
'''


# 函数的定义处,定义关键字收集参数
def my_func(a, b, c, **kwargs):
    print(a, b, c)
    print(kwargs)


my_func(a=1, b=2, c=3, d=10, e=21)

# 拼接任意长度的字符串
"""
班长:{} 刘浩杰
班花:{} 徐欣欣 + \n
"""


def my_func2(**kwargs):
    dictvar = {"monitor": "班长", "classflower": "班花"}
    str1 = ''
    str2 = ''
    for k, v in kwargs.items():
        if k in dictvar:
            str1 += dictvar[k] + ":" + v + '\n'
        else:
            str2 += v + ' '

    print(str1, "11")
    print(str2, "22")

my_func2(monitor="lll", classflower="hhh", ly="ly", hb="hb")
