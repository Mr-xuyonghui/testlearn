import unittest
from selenium import webdriver
import time
import unittest
from ddt import ddt,data,unpack
@ddt
class Test_ready(unittest.TestCase):
    def setUp(self) -> None:
        url='https://www.zhihu.com/signin?next=%2F'
        print("测试前准备开始")
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()
    def test_1(self):
        pass

    @data((1, '', '', "请输入手机号或邮箱"), (2, '1696669789', '123456789', "请输入正确的手机号"),(3, "13699999999", "xuyonghui0224", "该手机号尚未注册知乎"))
    @unpack
    def test01_login(self,id,name,pwd,result):
        '''验证知乎登陆N种情况'''
        #切换到密码登陆
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]').click()
        #通过name来查找元素
        self.driver.find_element_by_name('username').send_keys(name)
        self.driver.find_element_by_name('password').send_keys(pwd)
        #通过path来查找
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button').click()
        #无账号结果
        actresult_1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[2]/div/div').text
        #act = self.driver.find_element_by_class_name('SignFlowInput-errorMask undefined SignFlowInput-requiredErrorMask')
        #错误账号结果
        actresult_2 =self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[2]/div/div').text
        #账号未注册
        actresult_3=self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[2]/div/div').text
        if id == 1:
            self.assertEqual(actresult_1,result)
            #self.assertEqual(act, result)
        elif id == 2:
            self.assertEqual(actresult_2,result)
        elif id == 3:
            self.assertEqual(actresult_3,result)
if __name__ == '__main__':
    unittest.main(verbosity=2)