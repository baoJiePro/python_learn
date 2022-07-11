# ### return 返回值
"""
(1) return + 数据类型 :    将这个数据弹到函数的调用处,后面除了可以接六大标准数据类型之外,还可以返回类 对象 函数 等;默认返回None
(2) 函数当中,执行完return 之后,函数立刻终止,意味着函数里 , 跟在return后面的代码不执行
"""


# (1) 把数据返回到函数的调用处
def func():
    return [1, 2, 3, 4]


res = func()
print(res)


# (2) 函数的返回值不是必须的,按照需求来,如果不写return 返回值,默认返回None
def func():
    print(1234566)


# 打印1234567 和 自定义的return 之间没有半毛钱关系,返回值是自定义的;
print(1234567)
print(res)


def calc(sign, num1, num2):
    if sign == "+":
        res_value = num1 + num2
    elif sign == "-":
        res_value = num1 - num2
    elif sign == "*":
        res_value = num1 * num2
    elif sign == "/":
        res_value = num1 / num2
    else:
        return "算法错误"
    return res_value


res = calc("*", 1, 2)
print(res)
