# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 16:52

from multiprocessing import Process, Semaphore, set_start_method
import time, os


def ktv(person, sem):
    time.sleep(0.1)
    sem.acquire()
    print("%s进入ktv开始唱歌" % person)
    print(os.getpid())
    time.sleep(3)
    print("%s走出ktv离开" % person)
    sem.release()


if __name__ == "__main__":
    set_start_method("fork")
    sem = Semaphore(4)
    for i in range(10):
        p = Process(target=ktv, args=("person %s" % i, sem))
        p.start()
