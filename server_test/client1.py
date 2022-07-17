# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 01:25

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9000))
while True:
    message = input(">>>:")
    sk.send(message.encode("utf-8"))
    res = sk.recv(1024)
    if res == b'q':
        break
    print(res.decode("utf-8"))

sk.close()
