list = ["tom","amy","jack","pert"]
#求列表的长度
print("list的长度：",len((list)))
#通过索引取得某个值
print("索引为2的值：",list[2])
#通过appeng在末尾添加新值
list.append("newname")
print("append添加newname的list",list)
#通过insert插入数据
list.insert(3,"newname2")
print("在索引为3的位置插入新值",list)
#知道某个值的索引，通过del删除
#del list[3]

#知道某个值，但不知道所以用remove删除
list.remove("newname2")
print(list)

#通过pop（）弹出末尾的值，默认弹出最后一个，可以指定位置
#list_1=list.pop()
#print("pop()后list: ",list)
#print(list_1)

#通过pop弹出索引为2的值
#list_2 = list.pop(2)
#print("pop()后list: ",list)
#print(list_2)

#通过count计算列表中某个值出现的次数
#print(list.count("tom"))

#通过clear清空list
#list.clear()
#print(list)

#通过copy复制一个list
#list1=list.copy()
#print(list1)

#通过sort（）进行永久排序,默认升序
#list.sort()
#通过传入reverse=True 反序排序
#list.sort(reverse=True)
#print(list)

#通过sorted（）进行临时排序
print("通过sorted临时排序，不会改变原list :",sorted(list))
print("原list ：",list)

#通过index（）获得某个值的索引
print("amy的索引 ：",list.index("amy"))

#通过切片反序
print(list[::-1])

#切边不包括右边的索引
print(list[1:2])

#切边超过索引值，则全部出
print(list[1:200])

#index超过list长度会报valueerror错误
#print(list.index(200))

#list转元组
#tuple_2=tuple(list)
#print(tuple_2)

#list重复输出
print(list*3)

#list拼接 类似字符串
print(list+list)

#可以通过切片批量修改列表元素
print("切片赋值前：" ,list)
list[1:3] = ["a","b"]
print('list[1:3] = ["a","b"] 后:' ,list)