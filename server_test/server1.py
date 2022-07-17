# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 01:21
import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9000))
sk.listen()

while True:
    conn, addr = sk.accept()
    while True:
        msg = conn.recv(1024)
        print(msg.decode("utf-8"))
        message = input("我要发的数据>>>")
        conn.send(message.encode("utf-8"))
        if message == "q":
            break

