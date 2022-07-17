# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/18 00:27

from multiprocessing import Process, Queue

# q = Queue()
# q.put(111)
# res = q.get()
# print(res)
# 4.get_nowait 无论有没有都拿,如果拿不到,直接报错

# res = q.get_nowait()
# print(res)
# try:
#     res = q.get_nowait()
# except:
#     pass

# q = Queue(3)
# q.put(1)
# q.put(2)
# q.put(3)

# q.put(4)
def func(queue):
    res_data = queue.get()
    print("我是子进程", res_data)
    queue.put(2233)

if __name__ == "__main__":
    print("==============")
    q1 = Queue()
    p = Process(target=func, args=(q1,))
    p.start()

    q1.put("abcd")
    p.join()
    # 2.子进程添加的值,主进程通过队列拿到
    res = q1.get()
    print(res)
