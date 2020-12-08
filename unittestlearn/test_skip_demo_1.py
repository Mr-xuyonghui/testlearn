#coding=UTF-8
import unittest
class Test_skip(unittest.TestCase):
    num = 18
    def test_login(self):
        print("测试demo")

    def test_false(self):
        print("这是一个错误的测试")
        #self.assertEqual(1,2-3)

     #无条件条跳过
    @unittest.skip("该用例不用测试")
    def test_skip_1(self):
        print("这是一个跳过的测试用例")

    #条件判断为true时，跳过
    @unittest.skipIf(num > 16,"该用例不用测试")
    def test_skip_2(self):
        print("这是二个跳过的测试用例")

    #条件判断为false时跳过
    @unittest.skipUnless(num >19,"该用例不用测试")
    def test_skip_3(self):
        print("这是三个跳过的测试用例")



if __name__ == '__main__':
    print("main")
    unittest.main()