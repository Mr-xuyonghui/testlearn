import numpy as np
arr =np.arange(20).reshape(4,5)
print(arr)
#通过数组的transpose方法转置数组
print(arr.transpose())
#通过数组的t属性转置
print(arr.T)
print(arr)