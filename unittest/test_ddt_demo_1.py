import unittest
from ddt import ddt,data,
@ddt
class Test_ddt(unittest.TestCase):
    @data(10)
    def test01_onedata(self,args):
        print(args)
if __name__ == '__main__':
    unittest.main()