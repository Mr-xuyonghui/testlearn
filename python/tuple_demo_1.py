tuple_1 = ("a","b","c","d")
print("tuple_1 :",tuple_1)
print("tuple_1的长度",len(tuple_1))

#通过索引渠道元组元素
print("元组索引为1的值： ",tuple_1[1])

#元组元素是不能修改的
#tuple_1[1] = "p"

#元组解包
a,b,c,d = tuple_1
print("解组之后a的值 ",a)

#元组不可以修改，但是可以整体赋值
tuple_1 = ("e","f","t","y")
print("整体赋值之后的tuple_1:",tuple_1)

#tuple转list
tuple_list=list(tuple_1)
print("转为list：",tuple_list)