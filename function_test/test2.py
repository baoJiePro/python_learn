# ### 函数的参数
"""
参数:
(1)形参:形式参数 (在函数的定义处)
(2)实参:实际参数 (在函数的调用处)

形式参数种类: 普通(位置)参数 默认参数 普通收集参数 命名关键字参数 关键字收集参数
实际参数种类: 普通(位置)实参 关键字实参

形参和实参数量要一一对应
"""


# (1)普通形参
# 函数的定义处
# hang 和 lie 就是形参: 普通(位置)形参
def star(hang, lie=5):
    i = 0
    while i < hang:
        j = 0
        while j < lie:
            print("*", end="")
            j += 1

        print()
        i += 1


star(15, 20)


def star(hang, lie=20):
    print(hang, lie)


star(5)
star(hang=2, lie=5)
star(2)
star(lie=2, hang=10)
