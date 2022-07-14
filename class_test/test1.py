class MyClass:
    pass


class MyClass2(object):
    pass


obj = MyClass()


class MyClass3:
    color = "小汽车蓝色"

    def show_run(self):
        print("小汽车会跑")


obj = MyClass3()
obj.show_run()
print(obj.color)


class Car:
    price = "100万"
    __oil = "保密"

    def run(self):
        print("小车跑")

    def run2(self, info):
        print(info)

    def __oil_info(self):
        print("耗油")


obj = Car()

res = obj.price
print(res)

obj.run()
obj.run2(12)

obj.color = "屎黄色"
print(obj.color)
print(obj.__dict__)


def fang_xian_pan():
    print("mode fang xian pan")


obj.fang_xian_pan = fang_xian_pan
obj.fang_xian_pan()
print(obj.__dict__)


def hui_bi_xin(obj, name):
    print("我的小车,可以变成" + name, "价格是:" + obj.price)
obj.bianxing = hui_bi_xin

obj.bianxing(obj, "hello")

import types
obj.bianxing = types.MethodType(hui_bi_xin, obj)
obj.bianxing("hello ketty")
print(obj.__dict__)
