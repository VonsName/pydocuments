# __author: Administrator
# __date: 2018/8/6/006

from functools import reduce
import time


def test(a):
    return a * a


def func(a, b, f):
    return f(a) + f(b)


print(func(1, 2, test))

# func(1, 2, test)

# all 判断是否有空元素 参数必须是可迭代的
print(all([1, 2, "123"]))

# bool 判断一个表达式是否为True
print(bool(1 == 2))

# eval 计算
print(eval('1+3*2'))


# filter 过滤作用 参数是一个函数和一个可迭代数据
def fun1(a):
    if a != 1:
        return a


arr = [1, 2, 3]
ret = filter(fun1, arr)
print(ret)
print(list(filter(fun1, arr)))

# map 参数也是一个函数和一个可迭代序列
str1 = ['a', 'b']


def fun2(s):
    return s + 'hello'


res = map(fun2, str1)

print(list(res))


# reduce 根据函数做迭代器中所有值的运算
def add1(x, y):
    return x * y


print(reduce(add1, range(1, 7)))
print(reduce(add1, [1, 2, 3, 4, 5, 6, 7]))

# lambda 表达式
print(reduce(lambda a, b: a * b, [1, 2, 3, 4, 5]))


# 装饰器 函数作为参数
def show_time(f):
    def inner():  # 这里如果不使用闭包函数返回 则下面调用的时候只能使用foo调用 否则TypeError: 'NoneType' object is not callable
        # 如果使用了闭包函数返回，则下面的调用foo() 否则调用不生效
        start = time.time()
        f()
        end = time.time()
        print(end - start)

    return inner


# 调用的时候只能使用函数名 foo
@show_time  # foo=show_time(foo)
def foo():
    print("111")
    time.sleep(2)


# foo = show_time(foo)

# foo()
foo()
