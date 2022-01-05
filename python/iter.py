list = [1,2,3,4,5]
#创建可迭代队对象
l =iter(list)
#使用next输出元素
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#输出元素超量，会引起StopIteration异常
#print(next(l))
list1 = [1,2,3,4,5]
for i in list1:
    print("没有使用迭代器1:",i)
list1 = [1,2,3,4,5]
for i in list1:
    print("没有使用迭代器2:",i)

list2 = [1,2,3,4,5]
it = iter(list2)
for i in it:
    print("使用迭代器1:", i)
for i in it:
    print("使用迭代器2:", i)
