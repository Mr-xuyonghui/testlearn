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
    #指定默认运行某个测试用例，不指定默认为全部
    #unittest.main(defaultTest=Test_part.test_baidu)

    #通过addTest单个添加测试用例
    # #TestSuite() 不要忘记（）
    # suite=unittest.TestSuite()
    # suite.addTest(Test_part("test_baidu"))
    # suite.addTest(Test_part("test_bilibili"))
    # #defaultTest= '' 不要忘记单引号
    # unittest.main(defaultTest='suite')


    suite = unittest.TestSuite()
    testcase = [Test_part("test_baidu"),Test_part("test_bilibili")]
    suite.addTests(testcase)
    #unittest.main(defaultTest='suite')
    #TextTextRunner():unittest框架的TextTextRunner()类，通过该类下面的run()方法来运行suite所组装的测试用例，入参为suite测试套件。
    #unittest.TextTestRunner().run(suite)
    # print("当前文件文件名",os.path.abspath(__file__))
    # #获取当前文件所在文件夹名称
    dir_name=os.path.dirname(os.path.abspath(__file__))
    report_path=os.path.join(dir_name,"report")
    # #判断文件夹是否存在，不存在则创建
    if not os.path.exists(report_path):
          os.mkdir(report_path)
    #生成普通文档测试报告
    # file_path=os.path.join(report_path,"result.txt")
    # #生成html格式测试报告
    str_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    file_name ="resule"+str_time+".html"
    file_path = os.path.join(report_path, file_name)
    # with open(file_path,"w",encoding="utf-8")as f:
    with open(file_path, "wb") as f:
    #初始化运行器
        runner = HTMLTestRunner(f,verbosity=2,
                                title="这是个html格式的测试报告",
                                description="测试报告"
                                )
    #     runner=unittest.TextTestRunner(f,verbosity=2)
        runner.run(suite)
    suite = unittest.TestSuite()


    #自动查看当前目录下的所有测试用例
    #testcases=unittest.defaultTestLoader.discover(start_dir = os.getcwd(),pattern='*.py')
    #defaultTestLoader = TestLoader()
    #初始化加载器
    loader = unittest.TestLoader()
    #指定查找某个模块里面的测试用例
    #testcases = loader.loadTestsFromModule(test_skip_demo_1)
    #通过名称加载测试用例，入参为字符串
    #testcases = loader.loadTestsFromName('test_skip_demo_1.Test_skip.test_login')
    #通过名称加载测试用例，入参为列表，元素为字符串
    #testcases = loader.loadTestsFromNames(['test_skip_demo_1.Test_skip.test_login','test_skip_demo_1.Test_skip.test_false','test_skip_demo_1.Test_skip.test_skip_1'])
    #通过类名加载测试用例 模块名.类名
    #testcases = loader.loadTestsFromTestCase(test_skip_demo_1.Test_skip)
    #查找指定目录下的所有测试用例
    #testcases = loader.discover(start_dir=os.getcwd(),pattern='*.py')
    #print(testcases)
    #suite.addTests(testcases)
    #unittest.main(defaultTest='suite')