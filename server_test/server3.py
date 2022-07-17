# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 01:21
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 9000))

while True:
    msg, cli_addr = sk.recvfrom(1024)
    print(msg.decode("utf-8"))
    print(cli_addr)
    message = input(">>>>:")
    sk.sendto(message.encode("utf-8"), cli_addr)

sk.close()

