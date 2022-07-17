# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 01:04

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9000))

sk.send("早".encode("utf-8"))

res = sk.recv(1024)
print(res.decode("utf-8"))
sk.close()
