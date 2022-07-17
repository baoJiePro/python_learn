# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 15:26

from multiprocessing import Process
import time

def func():
    print("子进程start")
    time.sleep(2)
    print("子进程end")

if __name__ == "__main__":
    p = Process(target=func)
    p.daemon = True
    p.start()
    print("主进程执行结束")

