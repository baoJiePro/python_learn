from threading import Thread, Lock, RLock
import time

# ### (2) 递归锁
"""
递归锁,上几把锁,就解几把锁
"""
rlock = RLock()
def func(name):
    rlock.acquire()
    print(name, 1)
    rlock.acquire()
    print(name, 2)
    rlock.acquire()
    print(name, 3)
    rlock.release()
    rlock.release()
    rlock.release()

for i in range(10):
    t = Thread(target=func, args=("name%s" %i,))
    t.start()


