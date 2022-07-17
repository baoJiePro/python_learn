# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 15:43

from multiprocessing import Process, Lock, set_start_method
import json
import time


# lock = Lock()


# lock.acquire()
# lock.acquire()
# lock.release()
# lock.release()
# print(1111)

# with open("ticket_data.txt", mode="r", encoding="utf-8") as fp:
#     dic = json.load(fp)
#     print(dic)

def wr_info(sign, dic=None):
    if sign == "r":
        with open("ticket_data.txt", mode="r", encoding="utf-8") as fp:
            dic = json.load(fp)
        return dic
    elif sign == "w":
        with open("ticket_data.txt", mode="w", encoding="utf-8") as fp:
            json.dump(dic, fp)


def get_ticket(person):
    dic = wr_info("r")
    time.sleep(0.1)
    if dic["count"] > 0:
        print("%s抢到票了" % person)
        dic["count"] -= 1
        wr_info("w", dic)
    else:
        print("%s没有买到这个票" % person)


def ticket(person, lock_data):
    dic = wr_info("r")
    print("%s 查询余票: %s" % (person, dic['count']))
    lock_data.acquire()
    get_ticket(person)
    lock_data.release()


if __name__ == "__main__":
    set_start_method("fork")
    lock = Lock()
    # for i in range(10):
    #     ticket("person %s" % i, lock)
    for i in range(10):
        p = Process(target=ticket, args=("person %s" % i, lock))
        p.start()
