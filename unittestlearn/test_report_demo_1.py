from _datetime import datetime
import unittest
import os
from unittestlearn import test_skip_demo_1
from unittestlearn.HTMLTestRunner import HTMLTestRunner
class Test_part(unittest.TestCase):
    def test_baidu(self):
        print("这是第一个测试")

    def test_bilibili(self):
        print("这是第二个测试")

    def test_wangyi(self):
        print("这是第三个测试")

    def test_biying(self):
        print("这是第四个测试")
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_part('test_baidu'))
    suite.addTest(Test_part('test_biying'))
    # print("当前文件文件名",os.path.abspath(__file__))
    # #获取当前文件所在文件夹名称
    dir_name = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(dir_name, "report")
    # #判断文件夹是否存在，不存在则创建
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    # 生成普通文档测试报告
    # file_path=os.path.join(report_path,"result.txt")
    # with open(file_path,"w",encoding="utf-8")as f:
    #     runner=unittest.TextTestRunner(f,verbosity=2)
    #     runner.run(suite)
    #
    #生成html格式测试报告
    str_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    file_name = "resule" + str_time + ".html"
    file_path = os.path.join(report_path, file_name)
    with open(file_path, "wb") as f:
        # 初始化运行器
        runner = HTMLTestRunner(f, verbosity=2,
                                title="这是个html格式的测试报告",
                                description="测试报告"
                                )
        runner.run(suite)