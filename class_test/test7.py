# _*_ coding: utf-8 _*_

# @Author: BaoJie
# @time: 2022/7/16 10:07

import re

lst = re.findall("\d", "abcd ddd 345 sadfsfsdifsof23049__dfao29343458")
print(lst)
lst = re.findall("\D", "abcd ddd 345 sadfsfsdifsof23049__dfao29343458")
print(lst)

str_var = ' 					'
lst = re.findall("\s", str_var)
print(lst)

str_var = "  8989sdf 	111"
lst = re.findall("\S", str_var)
print(lst)

# ### 字符组 [123]
'''
[123] 必须从字符组当中挑出一个出来,个数上有要求,必须一个,如果匹配不到就是空.
'''
lst = re.findall("[123]", "sdfs3fkj5kj")
print(lst)

print(re.findall('a[abc]b', 'aab abb acb adb bab'))

# [0123456789] => [0-9] -是一个特殊字符,代表范围0-9 0到9
print(re.findall('a[0123456789]b', 'a1b a2b a3b a333b ayb'))
print(re.findall('a[0-9]b', 'a1b a2b a3b a333b ayb'))
print(re.findall('a[0-9a-zA-Z]b', 'a1b a2b a3b a333b ayb aAb'))
print(re.findall('a[0-9][*#/]b', 'a1/b a2b a29b a56b a456b'))
# 字符组当中的^ 代表除了的意思
# 除了+ - * / 这些字符之外,剩下的都能匹配
print(re.findall('a[^-+*/]b', "a%b ccaa*bda&bd"))

# 在特殊字符前面加商一个\,让原本有意义的字符变得无意义,用于正则字符匹配
print(re.findall('a[\^]b', "a^b"))

# 量词练习
'''1) ? 匹配0个或者1个a '''
print(re.findall("a?b", 'abbzab abb aab'))
'''2) + 匹配1个或者多个a '''
print(re.findall('a+b', 'b ab aaaaaab abb'))
'''3) * 匹配0个或者多个a '''
print(re.findall('a*b', 'b ab aaaaaab abbbbbbb'))
'''4) {m,n} 匹配m个至n个a '''
print(re.findall('a{1,3}b', 'aaab ab aab abbb aaz aabb'))

str_var = "刘能和刘大脑袋和刘铁锥子12子3"
lst = re.findall("刘.", str_var)
print(lst)
lst = re.findall("刘.?", str_var)
print(lst)
lst = re.findall("刘.+", str_var)
print(lst)
lst = re.findall("刘.*", str_var)
print(lst)
# lst = re.findall("刘.*子", str_var)
# print(lst)

# ###边界符练习 \b ^ $
# \b \bw 以w作为左边界  d\b 以d作为右边界
'''
\b 它默认是一个转义字符 退格 backspace  
需要通过字符串前面加上r,让转义字符失效,呈现正则的含义.
'''
lst = re.findall(r"d\b", "word pwd abc")
print(lst)

# ### ^ $
"""
如果使用了^ 或者 $ 
^ : 必须以某个字符开头,后面剩下的无所谓
$ : 必须以某个字符结尾,前面剩下的无所谓
意味着把这个字符串当成一个整体
"""
str_var = "大哥大嫂大爷"
print(re.findall('大.', str_var))
print(re.findall("^大.", str_var))

print(re.findall('(.*?)_good', 'wusir_good alex_good xboyww_good'))
print(re.findall('(?:.*?)_good', 'wusir_good alex_good xboyww_good'))
strvar = "5*4+6/8"
obj = re.search("\d+[*/]\d+", strvar)
res = obj.group()
print(res)
