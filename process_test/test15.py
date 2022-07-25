# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/23 11:01

'''
from gevent import monkey;monkey.patch_all()

import time
import gevent


def eat():
    print("eat one")
    time.sleep(1)
    print("eat two")
    return "吃完了"


def play():
    print("play one")
    time.sleep(1)
    print("play two")
    return "玩完了"


g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)

gevent.joinall([g1, g2])
print(g1.value)
print(g2.value)
print("主线程结束.")

'''
import time

'''

import requests
import gevent
import time

response = requests.get("http://www.baidu.com")
print(response)
res = response.status_code
print(res)
res_code = response.apparent_encoding
print(res_code)
response.encoding = res_code
res = response.text
print(res)
'''

"""
# 用消费者生产者模型扒网址
import re
strvar = r'<img hidefocus=true src="https://www.baidu.com/img/bd_logo1.png"  width=270 height=129>'
obj = re.search("src=(.*?) ",strvar)
res = obj.group()
res = obj.groups()[0]
"""

url_list = [
    "http://www.baidu.com",
    "http://www.4399.com",
    "http://www.7k7k.com",
    "http://www.jingdong.com",
    "http://www.taobao.com",
    "http://www.baidu.com",
    "http://www.4399.com",
    "http://www.7k7k.com",
    "http://www.jingdong.com",
    "http://www.taobao.com",
    "http://www.baidu.com",
    "http://www.4399.com",
    "http://www.7k7k.com",
    "http://www.jingdong.com",
    "http://www.taobao.com",
    "http://www.baidu.com",
    "http://www.4399.com",
    "http://www.7k7k.com",
    "http://www.jingdong.com",
    "http://www.taobao.com",
    "http://www.baidu.com",
    "http://www.4399.com",
    "http://www.7k7k.com",
    "http://www.jingdong.com",
    "http://www.taobao.com",
    "http://www.baidu.com",
    "http://www.4399.com",
    "http://www.7k7k.com",
    "http://www.jingdong.com",
    "http://www.taobao.com",
    "http://www.baidu.com",
    "http://www.4399.com",
    "http://www.7k7k.com",
    "http://www.jingdong.com",
    "http://www.taobao.com",
    "http://www.baidu.com",
    "http://www.4399.com",
    "http://www.7k7k.com",
    "http://www.jingdong.com",
    "http://www.taobao.com",
]

# import requests
# import gevent
# import time


# start_time = time.time()
# lst = []
# for i in url_list:
#     g = gevent.spawn(get_url, i)
#     lst.append(g)
#
# gevent.joinall(lst)
# end_time = time.time()
# print("------------------2")
# print(end_time - start_time, "<222222>")

import grequests
import requests

lst = []
start_time = time.time()
for i in url_list:
    rs = grequests.get(i)
    lst.append(rs)
data_list = grequests.map(lst)
for i in data_list:
    print(i.status_code)
end_time = time.time()
print(end_time-start_time)

rs = (grequests.get(u) for u in url_list)
response_list = grequests.map(rs, gtimeout=10)
for response in response_list:
    print(response)

# def get_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         # print(response.text)
#         pass
#
#
# start_time = time.time()
# for i in url_list:
#     get_url(i)
# end_time = time.time()
# print("--------------1")
# print(end_time - start_time, "<111111>")