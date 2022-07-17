# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 14:08
import time
from multiprocessing import Process
import os

# res = os.getpid()
# print(res)
#
# res = os.getppid()
# print(res)

# print("==========")

# def func():
#     print("1子进程id>>>:%s, 父进程id>>>:%s" % (os.getpid(), os.getppid()))
#
# if __name__ == "__main__":
#     print("2子进程id>>>:%s, 父进程id>>>:%s" % (os.getpid(), os.getppid()))
#     p = Process(target=func)
#     p.start()

# def func(n):
#     for i in range(1, n + 1):
#         time.sleep(0.3)
#         print("1子进程id>>>:%s, 父进程id>>>:%s" % (os.getpid(), os.getppid()))
#
#
# if __name__ == "__main__":
#     print("2子进程id>>>:%s, 父进程id>>>:%s" % (os.getpid(), os.getppid()))
#     p = Process(target=func, args=(10,))
#     p.start()

count = 99


def func():
    global count
    count += 1
    print("子进程id:%s" % (os.getpid()))
    print(count)


if __name__ == "__main__":
    p = Process(target=func)
    p.start()
    time.sleep(1)
    print("主进程：count=", count)
