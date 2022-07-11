# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/10 17:55

import pickle

dic = {"a": 1, "b": 2}
res = pickle.dumps(dic)
print(res, type(res))

res = pickle.loads(res)
print(res, type(res))

# dump  把对象序列化后写入到file-like Object(即文件对象)
with open("0512.txt", mode="wb") as fp:
    pickle.dump(dic, fp)
# load  把file-like Object(即文件对象)中的内容拿出来,反序列化成原来数据
with open("0512.txt", mode="rb") as fp:
    res = pickle.load(fp)

print(res, type(res))

import json

dic = {"name": "刘铁蛋", "age": 18, "sex": "女性", "family": ["father", "妈妈"], "agz": 1}
res = json.dumps(dic)
print(res, type(res))

with open("0512_2.txt", mode="w", encoding="utf-8") as fp:
    json.dump(dic, fp)

with open("0512_2.txt", mode="r", encoding="utf-8") as fp:
    res = json.load(fp)

print(res, type(res))

with open("0512_3.txt", mode="w", encoding="utf-8") as fp:
    json.dump(dic, fp)
    fp.write('\n')
    json.dump(dic, fp)
    fp.write('\n')

with open("0512_3.txt", mode="r", encoding="utf-8") as fp:
    for i in fp:
        res = json.loads(i)
        print(res, type(res))

dic = {"name": "刘铁蛋", "age": 18, "sex": "女性", "family": ["father", "妈妈"], "agz": 1}
with open("0512_4.txt", mode="wb") as fp:
    pickle.dump(dic, fp)
    pickle.dump(dic, fp)
    pickle.dump(dic, fp)
    pickle.dump(dic, fp)

with open("0512_4.txt", mode="rb") as fp:
    try:
        while True:
            res = pickle.load(fp)
            print(res)
    except:
        pass

import math
print(math.pi)
