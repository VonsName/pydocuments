#__author: Administrator
#__date: 2018/8/4/004
dic1={'name':'张是你','age':23}
print(dic1)
dic1['sex']='男'
print(dic1)
dic1.setdefault('name','默认')
print(dic1)
print(list(dic1.keys()))
#update 将dic2的数据加入到dic1,如果有重复的Key则覆盖
dic2={'name':'update','nini':'aaa'}
dic1.update(dic2)
print(dic1)
#删除 del
del dic1['nini']

#使用list把字典转换为列表
print(list(dic1))

#pop 删除
dic1.pop('sex')
print(dic1)

x=dic1.popitem()
print(x,dic1)

#
dic3=dict.fromkeys(['name','age','sex'],['lisi',23,'nv'])
print(dic3)
#字典相当于map 键值映射
dic4={'a':1,'b':2,'c':3}
for i in dic4:
    print(i,dic4[i])
for item in dic4.items():
    print(item)
for key in dic4.keys():
    print(key)
for value in dic4.values():
    print(value)