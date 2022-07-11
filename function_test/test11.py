# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/10 02:09


# ### 迭代器
set_var = {1, 2, "aa", "bb"}

# dir 获取当前数据内置的方法和属性.
lst = dir(set_var)
print(lst)
print("__iter__" in lst)

it = iter(set_var)
lst = dir(it)
print(lst)
print('__iter__' in lst and '__next__' in lst)
print("==============")
# 从collections模块 引入 Iterator类型(迭代器类型) Iterable(可迭代对象)
from collections.abc import Iterator, Iterable

res = isinstance(set_var, Iterable)
print(res)
res = isinstance(set_var, Iterator)
print(res)

it = iter(range(10))
print(isinstance(it, Iterable))
print(isinstance(it, Iterator))

# 使用for 和 next 搭配来遍历迭代器
for i in range(3):
    res = next(it)
    print(res)
