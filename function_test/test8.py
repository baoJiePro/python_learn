# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/9 15:06

# ### 函数的嵌套
"""
python中允许函数嵌套,嵌套在外层的是外函数,嵌套在里层的是内函数
"""


def func1():
    a = 10

    def func2():
        print(a)
        print(id)

    func2()


func1()

# (1)内部函数可以直接在函数外部调用么    不行
# (2)调用外部函数后,内部函数可以在函数外部调用吗  不行
# (3)内部函数可以在函数内部调用吗        可以
# (4)内部函数在函数内部调用时,是否有先后顺序 有


"""
#找寻变量的调用顺序采用LEGB原则(即就近原则)
B —— Builtin(Python)；Python内置模块的命名空间      (内建作用域)
G —— Global(module)； 函数外部所在的命名空间        (全局作用域)
E —— Enclosing function locals；外部嵌套函数的作用域(嵌套作用域)
L —— Local(function)；当前函数内的作用域            (局部作用域)
依据就近原则,从下往上 从里向外 依次寻找
"""

# ### nonlocal
"""
nonlocal 专门用来修饰[局部变量] 符合LEGB原则
(1)用来修改当前作用域上一层的[局部变量]
(2)如果上一层没有,继续向上寻找
(3)直到再也找不到了,直接报错
"""


# (1)用来修改当前作用域上一层的[局部变量]
def outer():
    a = 1

    def inner():
        nonlocal a
        a += 2
        print(a)

    inner()


outer()


# (2)如果上一层没有,继续向上寻找
def outer():
    a = 20

    def inner():
        a = 10

        def smaller():
            nonlocal a
            a += 2
            print(a)  # 12

        smaller()
        print(a)  # 12

    inner()
    print(a)  # 20


outer()

# (3)直到再也找不到了,直接报错
# a = 80  # 全局变量 nonlocal不能修饰
#
#
# def outer():
#     # a = 10
#     def inner():
#         def smaller():
#             nonlocal a
#             a += 2
#             print(a)  # 12
#
#         smaller()
#
#     inner()
#
#
# outer()
