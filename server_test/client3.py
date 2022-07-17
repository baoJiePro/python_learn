# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 01:25

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    msg = input(">>>>:")
    sk.sendto(msg.encode("utf-8"), ("127.0.0.1", 9000))

    message,ser_addr = sk.recvfrom(1024)
    print(message.decode("utf-8"))

sk.close()
