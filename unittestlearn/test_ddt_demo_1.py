import unittest
from ddt import ddt,data,unpack,file_data
@ddt
class Test_ddt(unittest.TestCase):
    #通过ddt可以传入python任意类型的数据
    #传入字符串，数据
    #@data(10)
    @data("name",10)
    def test01_onedata(self,args):
        print(args)

    @data(["name","age","sex"])
    @unpack
    def test02_muldata(self,name,age,sex):
        print("my namme is{},{} years old and a {}".format(name,age,sex))

    @data(["name","age","sex"])
    @unpack
    def test03_muldata(self,*args):
        print("通过nupack解包列表：",args)
    #*作用同解包list一样
    @data(*["name", "age", "sex"])
    def test04_muldata(self, args):
        print(args)

    @data(["name", "age", "sex"])
    #实参之后一个的话，形成为任意多个位置形参，数据会有问题
    #实际传入为：(['name', 'age', 'sex'],)
    def test05_muldata(self, *args):
        print(args)
    #通过file_data 可以导入json或者yaml格式文件
    @file_data("data.json")
    def test06_filedata(self,args):
        print(args)


if __name__ == '__main__':
    unittest.main()