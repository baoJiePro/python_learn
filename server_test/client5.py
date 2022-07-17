# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 09:46
import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9000))
sk.close()
