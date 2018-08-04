#__author: Administrator
#__date: 2018/8/4/004
arr=[1,2,3,4,5]
#for i in range(arr.__len__()):
 #   print(i)
#切片 会遍历最后一个值 最后一个参数是步长
print(arr[0:arr.__len__():1])

#不会遍历最后一个值
print(arr[0:-1])

#倒叙遍历
print(arr[arr.__len__()::-1])

#append 在末尾后面追加数据
arr.append("李四")
print(arr[arr.__len__()::-1])

#insert 在指定位置插入数据 原来位置的数据会向后移动
arr.insert(0,"张三")
print(arr[arr.__len__()::-1])

#通过切片修改多个值
print(arr[1:4])
arr[1:3]=['qq','aa']
print(arr[arr.__len__()::-1])

#删除 remove
arr.remove("aa")
print(arr[arr.__len__()::-1])
#删除并返回元素
name=arr.pop(0)
print(name)
print(arr[arr.__len__()::-1])

#删除整个数组
#del arr
#print(arr[arr.__len__()::-1])

#计算元素出现的次数
print(arr.count(3))


#extend
a=[1,2,3]
b=[2,3,5]
#把b的元素添加到a里面
a.extend(b)
print(a[0:])

#index 元素第一次出现的下标位置
print(a.index(3))

c=[4,5,6]
#顺序反转
c.reverse()
print(c)

#排序 自然顺序
d=[51,2,4,6,67]
#reverse=True 排序并且反转
d.sort(reverse=True)
print(d)

# name=input("请输入你的姓名:")
# age=input("请输入你的年龄:")
# salary=input("请输入你的工资:")
# print("你可以购买以下商品:")
# arr=["1. 苹果  300","2. 香蕉  300"]
# print(arr)

#元组 tuple 是只读的  不能被修改
a1=(1,2,3,4,5)
print(a1[0:])
#元组是只读的  不能被修改
#a1[1]=3