# ### 函数名的使用
# python中的函数可以像变量一样,动态创建,销毁,当参数传递,作为值返回,叫第一类对象.其他语言功能有限
# 1.函数名是个特殊的变量,可以当做变量赋值
def func():
    print("最近深圳暴雨死了不少人")


res = func
res()
print(type(res))


# 2.函数名可以作为容器类型数据的元素
def func1():
    print(11)


def func2():
    print(22)


def func3():
    print(33)


lst = [func1, func2, func3]
print(lst)
# 循环调用列表当中的每一个函数
for i in lst:
    i()

# 3.函数名可以作为函数的参数
print("<===>")


def func1(func_name):
    # 函数的调用处
    res_val = func_name()
    print(res_val)


# 函数的定义处
def func2():
    return 123


func1(func2)

'''
定义处就是def 声明的地方
调用处就是func()加上括号的地方
'''


# 4.函数名可作为函数的返回值
def func1(func2):
    # 返回到函数的调用处
    return func2


def func2():
    return 456


# 参数func2
res = func1(func2)
print(type(res))
print(res)
print(res())
