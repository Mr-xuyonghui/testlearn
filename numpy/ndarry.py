import numpy as np
arr =np.array([1,2,3,4,5,6])
print(arr)
#对数组的操作会应用到每个元素上---向量化
print(arr+arr)
print(arr*arr)
print(arr*2)
print(arr.shape)
print("数组数据类型"+str(arr.dtype))
print("几维数组"+str(arr.ndim))
print("一维数组切片"+str(arr[:3]))
#需要获得数组切片的拷贝需要现实调用
print(arr[:3].copy())
#
print(arr==1)
#在索引数组时可以传入布尔值数组,返回true的值
print(arr[arr==1])

#数组切片是原数组的视图，对切片修改会反应在原数组
arr[:3]=5
print(arr)
arr2d =np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(arr2d)
print(arr2d.shape)
print("数组数据类型"+str(arr2d.dtype))
print("几维数组"+str(arr2d.ndim))
#获取第一行数组
print(arr2d[1])
#获取第一行第一个数据
print(arr2d[1][0])
print(arr2d[1,0])
#获取第一行第一，二个数据
print(arr2d[1,0:2])
#获取所有行的第一二个数组
print(arr2d[:,0:2])

arr3d =np.array([[[1,2,3,4,5,6],[2,4,6,8,10,12]],[[9,7,6,5,4,3],[6,7,8,9,10,11]]])
print(arr3d[:])
print(arr3d[1][0])
print(arr3d[1,0])

#先生成0-20的一维数组，后转为4x5的二维数组
array=np.arange(20).reshape(4,5)
print(array)
#通过神奇索引选择1，3,4行
print(array[[0,2,3]])
#通过神奇索引选择1，3,4行中的第1，3，5个元素
print(array[[0,2,3],[0,2,4]])