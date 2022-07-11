# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/10 17:13

res = abs(-10)
print(res)

# round  四舍五入 (n.5 n为偶数则舍去 n.5 n为奇数，则进一!)
res = round(3.5)
print(res)
res = round(4.5)
print(res)

list_var = [1, 2, 34, 34, 43, 32, 5]
res = sum(list_var)
print(res)

res = max(list_var)
print(res)

res = min(list_var)
print(res)

list_var = [("张三", 45), ("李四", 38), ("王五", 18), ("田七", 120)]
def func(n):
    return n[-1]

res = min(list_var, key=func)
print(res)

# pow    计算某个数值的x次方
res = pow(4, 20)
print(res)

res = range(10)
print(res)

for i in range(1,16,3):
    print(i)

res = bin(15)
print(res)

res = "print(123)"
eval(res)

# exec   将字符串当作python代码执行(功能更强大)
res = """
for i in range(10):
	print(i)
"""
# 要注意小心sql注入 delete from 数据 where id = 1 exec或者eval两个函数慎用
exec(res)

res1 = "今天天气好"
res2 = "今天天气好"
res3 = "132"

print(hash(res1))
print(hash(res2))
print(hash(res3))
