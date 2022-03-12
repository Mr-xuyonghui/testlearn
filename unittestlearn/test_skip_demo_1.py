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
        print("这是一个无条件跳过的测试用例")

    #条件判断为true时，跳过
    @unittest.skipIf(num > 16,"该用例不用测试")
    def test_skip_2(self):
        print("这是一个条件成立则跳过的测试用例")

    #条件判断为false时跳过
    @unittest.skipUnless(num >19,"该用例不用测试")
    def test_skip_3(self):
        print("这是一个条件不成立则跳过的测试用例")
    @unittest.expectedFailure
    def test_skipe_4(self):
        self.assertEqual(1,18,"1不等于18")
        print("这是运行错误但标记为通过的测试用例")


#需要通过python运行才会执行
if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Test_skip('test_login'))
    # suite.addTests([Test_skip('test_login'),Test_skip('test_false')])
    # runner=unittest.TextTestRunner()
    # runner.run(suite)