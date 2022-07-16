# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/16 01:10

import os


class ReadFile:
    def __new__(cls, name):
        if os.path.exists(name):
            return object.__new__(cls)

        return print("没有这个文件")

    def __init__(self, name):
        self.fp = open(name, "r", encoding="utf-8")

    def read_content(self):
        res = self.fp.read()
        return res

    def __del__(self):
        self.fp.close()


obj = ReadFile("aa.txt")
print(obj)
res = obj.read_content()
print(res)

# ### #__call__ 魔术方法
'''
	触发时机：把对象当作函数调用的时候自动触发
	功能: 模拟函数化操作
	参数: 参数不固定,至少一个self参数
	返回值: 看需求
'''


# (1) 基本用法
class MyClass:
    def __call__(self):
        print("call 方法被调用")


# pass

obj = MyClass()
obj()


class Cat:
    gift = "抓老鼠"

    def __init__(self, name):
        self.name = name

    def cat_info(self):
        str_var = "这个对象叫{},小猫天生就会{}".format(self.name, self.gift)
        return str_var

    def __str__(self):
        return self.cat_info()


tom = Cat("tom")
res = tom.cat_info()
print(res)
print(tom)

res = str(tom)
print(res)

list_var = [1, 2, 3, 4, 5]
print(len(list_var))
