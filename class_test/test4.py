class MyClass:
    abc = "123"

    def __new__(cls, *args, **kwargs):
        print("123")
        return object.__new__(cls)


obj = MyClass()
print(obj)
print(obj.abc)


class Boat:
    def __new__(cls, *args, **kwargs):
        print(1)
        return object.__new__(cls)

    def __init__(self, *args, **kwargs):
        print(2)
        strvar = ""
        for i in args:
            strvar += i + " "
        print(strvar)
        print(kwargs)


obj = Boat("周杰伦", "李宇春", "周星驰", name="韩庚")
