from queue import Queue

q = Queue()
q.put(11)
q.put(22)
print(q.get())
print(q.get())

q2 = Queue(2)
q2.put(33)
q2.put(44)
# q2.put(55)

# (2) LifoQueue 后进先出 (数据结构中,栈队列的一种储存顺序)
from queue import LifoQueue
lq = LifoQueue()
lq.put(55)
lq.put(66)
print(lq.get())
print(lq.get())

# (3) PriorityQueue 按照优先级顺序排列
from queue import PriorityQueue
pq = PriorityQueue()
pq.put((12, "zs"))
pq.put((5, "ls"))
pq.put((8, "ww"))
pq.put((8, "wa"))
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())

