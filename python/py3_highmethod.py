"""
map()内置函数，将方法映射到每一个元素中
"""
from functools import reduce


def fmap(a, b):
    return (a, b)


lik = range(1, 11)
liv = list("abcdefghij")
# lim = map(fmap, lik, liv)
lim = map(lambda a, b: (a, b), lik, liv)
for k, v in lim:
    print("key is {},value is {}".format(k, v))

# lim =dict(lim)
# print(type(lim))
# for k,v in lim.items():
#         print("key is {},value is {}".format(k,v))

"""
lamdba 定义匿名函数，减少不可复用函数
"""
a = map(lambda x: x + 1, [1, 2, 3])
for i in a:
    print(i)

"""
zip打包,*解包
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 10]
e = zip(a, b)
# 以短的列表为界限
f = zip(a, c)
print("e type is {},value is {}".format(type(e), list(e)))
print("f type is {},value is {}".format(type(f), list(f)))
g, h = zip(*zip(a, b))
print(g, h)

"""
filter，过滤器，过滤函数结果为false的，保留true的
"""


def is_odd(n):
    return n % 2 == 1


# tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tmplist = filter(lambda n: n % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)

"""
enumerate()遍历函数，遍历可迭代对象，一般用于for循环中，返回inde和value
"""

a = ["a", "b", "c", "d"]
# 没有设置起始角标
print(list(enumerate(a)))
# 设置起始角标
print(list(enumerate(a, start=1)))
for index, value in enumerate(a):
    print(index, value)

"""
reduce(),对参数化序列，列表或者元组进行累积
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add(x, y):
    return x + y

#b = reduce(add, a)
b = reduce(lambda x, y: x + y, a)
print(b)
