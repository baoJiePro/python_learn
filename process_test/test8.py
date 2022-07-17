# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/18 00:59

from multiprocessing import Process
from threading import Thread, currentThread, active_count
import random, time, os


# def func(num):
#     time.sleep(random.uniform(0.1, 1))
#     print("子线程", num, os.getpid())
#     pass
#
# if __name__ == "__main__":
#     for i in range(10):
#         t = Thread(target=func, args=(i,))
#         t.start()

def func(i):
    # time.sleep(random.uniform(0.1,1))
    print("子线程", i, os.getpid())


if __name__ == "__main__":
    startime = time.perf_counter()
    lst = []
    for i in range(1000):
        t = Thread(target=func, args=(i,))
        t.start()
        lst.append(t)
    for i in lst:
        i.join()
    endtime = time.perf_counter()
    print(endtime - startime, "主线程执行结束===================")


    # startime = time.perf_counter()
    # lst = []
    # for i in range(1000):
    #     p = Process(target=func, args=(i,))
    #     p.start()
    #     lst.append(p)
    # for i in lst:
    #     i.join()
    # endtime = time.perf_counter()
    # print(endtime - startime, "主进程执行结束======================")
print(active_count())
