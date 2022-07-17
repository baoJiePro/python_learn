# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/16 23:42

import socket

# 1.创建一个socket对象  # 默认返回tcp协议的对象
sk = socket.socket()
# 2.绑定ip和端口 (把该主机注册到网络里,让别人找到你)
# 127.0.0.1 默认指代本机的ip地址
sk.bind(("127.0.0.1", 9000))
# 3.开启监听
sk.listen()

# 4.三次握手 conn 是建立三次握手之后返回的对象, addr 是对方的ip地址
# accept() 必须建立好握手之后,下面的代码才能执行,因为其中加了阻塞.
# 比如input sleep.. 都是程序内部加了阻塞.
conn, addr = sk.accept()

# 5.写收发消息的逻辑
# ...
# 服务端接收消息 同一时间最多最多接收1024个字节
msg = conn.recv(1024)
print(msg.decode("utf-8"))
conn.send("你也早".encode("utf-8"))


# 6.四次挥手
conn.close()
# 7.退还端口
sk.close()
