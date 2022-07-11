# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/10 14:19

lst = [1, 2, 3, 4, 4, 5, 9, 6]
res = [i for i in lst if i % 2 == 1]
print(res)

list_var = ["a", "b", "c", "d"]
res = enumerate(list_var)
print(res)
print(list(res))

dict_var = {a: b for a, b in enumerate(list_var, start=7)}
print(dict_var)

res = dict(enumerate(list_var, start=8))
print(res)

list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 99, 0, 0]

it = zip(list1, list2)
print(list(it))


