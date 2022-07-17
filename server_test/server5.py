# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/17 09:46

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("---->执行")
        print(self.request)
        print(self.client_address)

# 生成一个对象
# ThreadingTCPServer( "ip端口号" ,"自定义的类"  )
server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
# 循环调用
server.serve_forever()
