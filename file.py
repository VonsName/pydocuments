#__author: Administrator
#__date: 2018/8/4/004
import  sys
#打开一个文件 第二个参数为打开模式 r 表示读取
file=open('笔记1','r',encoding='utf-8')
#读取
#data=file.read()

#a 表示会在后面追加内容
#w=open('笔记1','a',encoding='utf-8')
#w.write('python写')
#print(data)

#只读取一行数据
linedata=file.readline()
print(linedata)

#返回一个列表 读取所有的数据
print(file.readlines())


for item in file.readlines():
    print(item.strip())
#关闭
file.close()

with open('笔记','r',encoding='utf-8') as f:
    f.readlines()

a=[1,2,3]
b=a.copy()
print(b)