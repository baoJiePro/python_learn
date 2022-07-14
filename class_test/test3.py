class Father:
    f_property = "111"
    def f_hobby(self):
        print("222")
class Human:
    def f_hobby(self):
        print("5555")
class Mother:
    m_property = "333"
    def m_hobby(self):
        print("444")

class Daughtor(Father, Mother, Human):
    def s_skill(self):
        print(super().m_hobby())
        # print(super().f_hobby())


obj = Daughtor()
# obj.f_hobby()
# obj.m_hobby()
print("====")
obj.s_skill()

res = issubclass(Daughtor, Mother)
print(res)

