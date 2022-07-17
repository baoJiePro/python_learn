# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 01:21
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 9000))

msg, cli_addr = sk.recvfrom(1024)
print(msg.decode("utf-8"))
sk.close()

