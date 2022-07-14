import os

# os.system("ifconfig")
os.system("pwd")

res = os.popen("pwd").read()
print(res)

# res = os.popen("ifconfig").read()
# print(res)

lst = os.listdir("/")
print(lst)
#  获取当前文件所在的默认路径
res = os.getcwd()
print(res)

lst = os.listdir(res)
print(lst)
# 创建文件夹
# os.mkdir("test")

# os.makedirs("aa")
# os.removedirs("test")

# os.remove("0512.txt")
# os.rename("0512_2.txt", "0512_22.txt")

import shutil

with open("a.txt", mode="a+", encoding="utf-8") as fp:
    fp.write("hahaha")

shutil.copy("a.txt", "test/b.txt")

res = os.environ
print(res)

print(os.name)
print(os.sep)

res = os.path.abspath(".")
print(res)

path1 = "home"
path2 = "aa"
path3 = "bb"
res = os.path.join(path1, path2, path3)
print(res)


