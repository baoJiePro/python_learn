# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/16 00:34

class Singleton:
    __obj = None

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

obj1 = Singleton()
print(obj1)
obj2 = Singleton()
print(obj2)
obj3 = Singleton()
print(obj3)


class Singleton2:
    __obj = None

    def __new__(cls, name):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self, name):
        self.name = name

    def __del__(self):
        # print("析构函数被执行")
        pass

obj1 = Singleton2("aa")
obj2 = Singleton2("bb")
print(obj1)
print(obj2)
print(obj1.name)
print(obj2.name)
print("===============")

class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("dog {} like eat".format(self.name))

    def __del__(self):
        print("析构方法被触发")


obj = Dog("cat")
obj2 = Dog("kitty")
obj.eat()
# del obj
obj2.eat()
print("======end======")
