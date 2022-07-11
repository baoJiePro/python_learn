# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/9 14:57

# ### 全局变量  和 局部变量
"""
局部变量: 定义在函数里面的变量就是局部变量
全局变量: 定义在函数外面的变量或者在函数内部用global关键字声明的变量是全局变量
局部变量的作用域: 只限定在函数内部
全局变量的作用域: 横跨整个文件
"""

# (3)在函数内部可以通过global关键字修饰,进而修改全局变量
# 注意点:务必在函数这个代码块的开头用global关键字声明修饰
c = 12


def func3():
    global c
    c += 2
    print(c)


func3()

# (4)可以在函数内部直接声明一个全局变量
def func4():
    global d
    d = 90
    d += 10
    print(d)

func4()
print(d)

"""
global 关键字如果在函数外面有该全局变量,用在函数中是修改全局变量
global 关键字如果在函数外面没有该全局变量,用在函数中是定义全局变量
"""
