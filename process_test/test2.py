# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 15:06

# print(__name__)
# print(type(__name__))

from multiprocessing import Process

import os


def func(num):
    print("发送第%i封邮件" % num)


if __name__ == "__main__":
    for i in range(1, 5):
        p = Process(target=func, args=(i,))
        p.start()
        p.join()
    print("发送主邮件")


class MyProcess(Process):
    def run(self) -> None:
        print("1子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(), os.getppid()))

print("------------")
if __name__ == "__main__":
    p = MyProcess()
    p.start()
    print("主进程:{}".format(os.getpid()))

class MyProcess2(Process):
    def __init__(self, arg):
        # 调用一下父类的构造方法来进行初始化
        super().__init__()
        self.arg = arg

    def run(self) -> None:
        print("1子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(), os.getppid()))
        print(self.arg)


if __name__ == "__main__":
    lst = []
    for i in range(10):
        p = MyProcess2("参数:%s" % (i))
        p.start()
        lst.append(p)

    for i in lst:
        i.join()

    print("最后执行子进程这句话:", os.getpid())