# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/10 02:55

from collections.abc import Iterator, Iterable

list_var = ["1", "2", "3", "4"]
it = map(int, list_var)
print(isinstance(it, Iterable))
print(isinstance(it, Iterator))

# for i in it:
#     print(i, type(i))

# (3)list 类型强转 使用list强转迭代器可以瞬间拿到迭代器中所有数据
lst = list(it)
print(lst)


def func(n):
    return n * 2


lst = [1, 2, 3, 4]
it = map(func, lst)
print(list(it))

lst = [5, 4, 9, 9]
it = iter(lst)
total = 0
for i in it:
    total = total * 10 + i
print(total)

from functools import reduce


def func(x, y):
    return x * 10 + y


lst = [5, 4, 9, 9]
res = reduce(func, lst)
print(res)

list_var = [1, 2, -88, 30, 15]
res = sorted(list_var)
res = sorted(list_var, reverse=True)
res = sorted(list_var, key=abs)
print(res)

list_var = [19, 23, 44, 57]


def func(n):
    return n % 10


res = sorted(list_var, key=func)
print(res)

list_var = [4, 1, 2, 9]
list_var.sort()
print(list_var)

list_var = [1, 2, 3, 4, 4, 56, 6, 6, 7, 8, 9, 10]


def func(n):
    if n % 2 == 0:
        return True
    else:
        return False


it = filter(func, list_var)
res = list(it)
print(res)

it = filter(lambda n: True if n % 2 == 0 else False, list_var)
print(list(it))
