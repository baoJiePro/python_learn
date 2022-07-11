fp = open("0414_4.txt", mode="a+", encoding="utf-8")
fp.write("今天晚上要早走111")
res = fp.tell()
print(res)
fp.seek(2)
res = fp.tell()
print(res)
fp.close()

with open("0404_6.txt", mode="a+", encoding="utf-8") as fp:
    fp.write("abcdefg我是你好")
    fp.seek(0)  # fp.seek(0,2) 移动到文件的末尾
    res = fp.read()
    print(res)

# 简化文件复制操作  open 之间 可以用逗号,隔开 为了简化操作
with open("0404_6.txt", mode="r", encoding="utf-8") as fp1, open("0404_6_copy.txt", mode="w+", encoding="utf-8") as fp2:
    res = fp1.read()
    fp2.write(res)
    fp2.seek(0)
    res = fp2.read()
    print(res)

# 刷新缓冲区 flush
# 当文件关闭的时候自动刷新缓冲区
# 当整个程序运行结束的时候自动刷新缓冲区
# 当缓冲区写满了  会自动刷新缓冲区
# 手动刷新缓冲区
fp = open("0414_7.txt", mode="w+", encoding="utf-8")
fp.write("测试close")
fp.flush()
fp.close()

# (1)readline()     功能: 读取一行文件内容
"""
readline(字符个数) 单位读的时字符的个数
如果当前字符个数 > 实际个数 那就只读当前行
如果当前字符个数 < 实际个数 那就按照给与的当前个数读取 
"""
''''''
# 读出所有行数 每一行都读
fp = open("0414_8.txt", mode="r+", encoding="utf-8")
res = fp.readline()
# 判断res是不是为空,如果不是空,则进去打印该字符串
while res:
    print(res)
    res = fp.readline()  # 读到最后是一个'' bool('') => False
fp.close()


list_var = []
with open("0414_8.txt", mode="r+", encoding="utf-8") as fp:
    res = fp.readlines()
    # 过滤数据
    for i in res:
        res = i.strip()
        list_var.append(res)
print(list_var)


