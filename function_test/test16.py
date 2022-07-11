# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/11 00:56

import random
res = random.random()
print(res)

res = random.randrange(1, 10)
print(res)

def rand_data():
    str_var = ""
    for i in range(5):
        a_z = chr(random.randrange(97,123))
        A_Z = chr(random.randrange(65,91))
        num = str(random.randrange(0,10))
        list_var = [a_z,A_Z, num]
        str_var += random.choice(list_var)
    return str_var

res = rand_data()
print(res)

import time

res = time.time()
print(res)

