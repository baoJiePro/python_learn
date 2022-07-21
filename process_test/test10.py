import random
import time
from threading import Thread, Lock, Semaphore

n = 0
lst = []

def func1(lock_data):
    global n
    for i in range(100000):
        lock_data.acquire()
        n -= 1
        lock_data.release()


def func2(lock_data):
    global n
    for i in range(100000):
        with lock_data:
            n += 1

def func(i, sem):
    time.sleep(random.uniform(0.1, 1))
    with sem:
        print(i)
        time.sleep(random.uniform(3, 6))


if __name__ == "__main__":
    lock = Lock()
    for i in range(10):
        t1 = Thread(target=func1, args=(lock,))
        t2 = Thread(target=func2, args=(lock,))
        t1.start()
        t2.start()
        lst.append(t1)
        lst.append(t2)

    for i in lst:
        i.join()

    print(n)

    sem = Semaphore(5)
    for i in range(20):
        Thread(target=func, args=(i, sem)).start()


