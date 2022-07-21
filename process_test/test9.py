from threading import Thread
import time

def func1():
    while True:
        print("我是线程1，func1")

def func2():
    print("我是线程2，start")
    time.sleep(3)
    print("我是线程2，end")

t1 = Thread(target=func1)
t1.setDaemon(True)
t1.start()

t2 = Thread(target=func2)
t2.start()

print("主线程执行结束")
