from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os, time


def func(i):
    print("process: ", i, os.getpid())
    time.sleep(3)
    print("process: end")
    return 5488


# if __name__ == "__main__":
#     p = ProcessPoolExecutor()
#     res = p.submit(func, 1)
#     for i in range(10):
#         res = p.submit(func, i)
#     print(res, type(res))
#     res2 = res.result()
#     print(res2)
#     p.shutdown()
#     print("down")

from threading import current_thread as cthread


def func2(i):
    print("thread", i, cthread().ident)
    time.sleep(3)
    return cthread().ident


tp = ThreadPoolExecutor(5)
for i in range(10):
    res = tp.submit(func2, i)
tp.shutdown()

