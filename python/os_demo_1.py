import os
#获取当前文件所在的相对路径
localraod = os.getcwd()
print("文件的相对路径：",localraod)
#获取绝对路径，每次都相同
absroad=os.path.abspath("os_demo_1.py")
print("文件的绝对路径：",absroad)
#判断路径是否是文件夹
print("路径是否是文件夹: ",os.path.isdir(localraod))
#isabs()有待学习
print("路径是否是绝对路径： ",os.path.isabs("/Users/iyourcar/python-example/learning"))
print("路径是否是绝对路径： ",os.path.isabs("Users/iyourcar/python-example/learning"))
#判读路径下是否是文件
print("路径是否是文件：",os.path.isfile(absroad))
makedir = os.path.join(localraod,"newdir")
print(makedir)
#创建一个文件夹
#os.mkdir(makedir)
#创建一个文件需要用到open方法
#file=os.path.join(makedir,"newfile.txt")
#print("新建文件路径：",file)
#with open(file,mode="w") as f:
#    f.write("这是一个新建的文件")
#判断文件或者目录是否存在
#print("newfile.txt文件是否存在：",os.path.exists(file))
#print("newfile文件夹是否存在：",os.path.exists(os.path.join(makedir,"newfile")))
#获取当前路径下目录列表
print(os.listdir())
#删除空文件夹--文件夹不为空删除报错
# os.rmdir(makedir)