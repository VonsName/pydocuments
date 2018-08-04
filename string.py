#__author: Administrator
#__date: 2018/8/4/
import sys
a='hello'
b='world'
print(a+b)
c="".join([a,b])
print(c)
print(c.count('l'))
#首字母大写
print(c.capitalize())

print(sys.getdefaultencoding())

x=input(">>>:").strip()
print(x)