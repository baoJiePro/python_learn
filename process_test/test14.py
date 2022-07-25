import time


def gen():
    for i in range(10):
        yield i


mygen = gen()


# for i in mygen:
#     print(i)

# for i in range(3):
#     res = next(mygen)
#     print(res)

def producer():
    for i in range(100):
        yield i


def consumer():
    g = producer()
    for i in g:
        print(i)


# consumer()
'''
from greenlet import greenlet

def eat():
    print("eat one")
    g2.switch()
    time.sleep(1)
    print("eat two")

def play():
    print("play one")
    time.sleep(1)
    print("play two")
    g1.switch()

g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch()
'''

'''
import gevent
def eat():
    print("eat one")
    gevent.sleep(1)
    print("eat two")

def play():
    print("play one")
    gevent.sleep(1)
    print("play two")

g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)
g1.join()
g2.join()
print("主线程执行完毕")
'''

from gevent import monkey

monkey.patch_all()
import time
import gevent


def eat():
    print("eat one")
    time.sleep(1)
    print("eat two")


def play():
    print("play one")
    time.sleep(1)
    print("play two")

g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)

g1.join()
g2.join()