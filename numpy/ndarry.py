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
#获取第一样第一二个数据
print(arr2d[1,0:2])
print(arr2d[:,0:2])
