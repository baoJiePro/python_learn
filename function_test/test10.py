# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/9 21:29

# ### locals 和 globals

# (1)locals()  :返回字典,获取当前作用域的所有内容
"""
    如果在函数里:获取locals()调用之前,该作用域出现的内容
    如果在函数外:获取locals()打印返回值之前,该作用域出现的内容
"""
# (1)所在作用域是全局命名空间,打印res之前的所有获取内容

a = 1
b = 2
print(locals())
print(globals())

dic = globals()
dic['wangwen'] = "风流倜傥,高大威猛,威武帅气,万人迷"
# print(wangwen)

# ### 匿名函数 lambda表达式
"""
lambda表达式 : 用一句话来表达只具有返回值的函数,简单,方便,直截了当
# 语法:
lambda 参数 :  返回值 

"""


def func():
    return "今天"


func = lambda: "今天新来的女生真漂亮"

res = func()
print(res)

# (2) 有参数的lambda 表达式
func = lambda n: type(n)

res = func(10)
print(res)

func = lambda n: "偶数" if n % 2 == 0 else "基数"

res = func(3)
res = func(12)
print(res)

func = lambda n, m: n if n > m else m

res = func(10, 20)
print(res)
