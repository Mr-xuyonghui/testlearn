import unittest
from parameterized import parameterized

class Test_data(unittest.TestCase):
    #传递一个list，里面为tuple
    @parameterized.expand([('xuyonghui',26),('xujiahui',24)])
    def test_01(self,name,age):
        print("my name is{},age is {}".format(name,age))

if __name__ == '__main__':
    unittest.main()