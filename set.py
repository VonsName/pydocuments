#__author: Administrator
#__date: 2018/8/4/004


#set 会去重 唯一性
a=set('lisi')
s1=['wangwu','wangwu','zhangsna']
#列表转set
s2=set(s1)
print(a)#{'l', 'i', 's'}

print(s2)

s3=[['a','b'],1,2,3]

#列表转set的键必须是可以hash的
#s4=set(s3)#TypeError: unhashable type: 'list'
#print(s4)

print(21 in s3)
s2.add('ccc')
print(s2)

#更新内容 会把每个字符添加进set,不会重复
s2.update('dfs')
print(s2)

#清空
s2.clear()
print(s2)


print(set('aaa') == set('aaabbv'))
print(set('aaa') < set('aaavv'))

print(set('abv') or set('aox'))
print(set('abv') and set('aox'))

a=set([1,2,3])
b=set([3,4,5])
#交集
print(a.intersection(b))
print('交集',a&b)
#并集
print(a.union(b))
print("并集",a|b)
#差集
print(a.difference(b))
print("差集",a-b)
#对称差集 两个set在对方都没有的
print(a.symmetric_difference(b))
print('对称差集',a ^ b)
#超集
print('超集', a.issubset(b))
#子集
print('子集', a.issubset(b))
#14-3
