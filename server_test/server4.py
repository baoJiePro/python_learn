# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 09:34

import socket
import struct
sk = socket.socket()

sk.bind(("127.0.0.1", 9000))
sk.listen()

conn, addr = sk.accept()
# 收发数据的逻辑
# ...
inp = input(">>>msg:")
msg = inp.encode("utf-8")
res = struct.pack("i", len(msg))
conn.send(res)

conn.send(msg)

conn.send("world".encode("utf-8"))

# 四次挥手
conn.close()
# 退回端口
sk.close()
