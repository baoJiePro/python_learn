# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/18 00:43

from multiprocessing import Process, Queue, set_start_method
import random, time


def consumer(queue, name):
    while True:
        food = queue.get()
        if food is None:
            break
        time.sleep(random.uniform(0.1, 1))
        print("%s 吃了一个%s" % (name, food))
    pass


def producer(queue, name, food):
    for i in range(3):
        time.sleep(random.uniform(0.1, 1))
        print("%s 生产了 %s,%s" % (name, food, i))
        queue.put(food + str(i))


if __name__ == "__main__":
    set_start_method("fork")
    q = Queue()
    c1 = Process(target=consumer, args=(q, "kitty"))
    c1.start()

    p1 = Process(target=producer, args=(q, "anJin", "tudou"))
    p1.start()
    p1.join()
    q.put(None)
