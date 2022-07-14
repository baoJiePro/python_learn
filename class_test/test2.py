class Plane:
    captain = "anJin"
    __air_sister = 20

    def fly(self):
        print("飞机会飞")

    def fly2():
        print("灰机会飞2")

print(Plane.captain)
Plane.fly2()

obj = Plane()
obj.fly()

Plane.logo = "747"
print(Plane.logo)

print(Plane.__dict__)
print(obj.logo)

class Human:
    skin = "黝黑"
    hair = "黑色"

    def study(self):
        print("study")

    def __sex(self):
        print("sex")


class Man(Human):
    pass

obj = Man()
print(obj.hair)


# class Woman(Human):
#     def myskill(self):
#         self.__sex()
#
# obj = Woman()
# obj.myskill()

