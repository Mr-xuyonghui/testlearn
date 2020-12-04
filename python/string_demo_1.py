new_str = "这是一个字符串呀"
#根据索引位置取值
print(new_str[0])
#通过index找到某个值的索引
print(new_str.index("是"))
#字符串切片,没有步长
print(new_str[0:4])
#字符串切片，有步长,按步长2切取0-4索引字符
print(new_str[0:4:2])
#字符串反向 切取所有，从-1位置开始，即从末尾向前开始切
print(new_str[::-1])

new_str_1="这是第二个字符串呀"
#通过+号连接字符串
str = new_str + new_str_1
print(str)
#通过join连接字符串，不添加额外字符
str_1 = "".join([new_str,new_str])
print(str_1)
#通过join连接字符串，添加额外字符
str_2 = "-".join([new_str,new_str])
print(str_2)

new_str_3 = new_str + new_str_1 + "这是第三个字符串"
#通过split拆分字符串,返回一个list
print("new_str_3:",new_str_3)
#通过split拆分，不设置字数
print(new_str_3.split("这"))
#通过split拆分设置字符
print("只拆分第一个这：",new_str_3.split("这",2))
print(type(new_str_3.split("这")))
