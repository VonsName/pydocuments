# __author:  Administrator
# __date:  2018/8/6/006


# 列表生成式

def f(x):
    return x ** x  # x的x次幂


a = [f(i) for i in range(10)]
a1 = [f(i) for i in range(10)]

print(a)
print(a1)
print(0 ** 0)
print(type(a))

# 类似解构赋值
t = (2, 3)
j, y = t
print(j, y)

# 生成器 generator  它是一个可迭代对象  # 超过范围报错 StopIteration
s = (i * 2 for i in range(5))
print(s)
print('s.next', s.__next__())
print('s.next', s.__next__())
print('s.next', s.__next__())
print(next(s))
print(next(s))
# print(next(s))
