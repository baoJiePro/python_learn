# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 01:25

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.sendto("你好".encode("utf-8"), ("127.0.0.1", 9000))
sk.close()
