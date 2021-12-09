import unittest
from selenium import webdriver
from seleniumlearn.PageOjects.LoginPages import LoginPage
from ddt import ddt,data,unpack
from seleniumlearn.TestDatas.LoginDatas import Login_account
from seleniumlearn.BasePages import BasePage
@ddt
class Test_login(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://res.youcheyihou.com/test/backend/newsadmin/index.html#/login")
    def tearDown(self) -> None:
        self.driver.quit()
    @data((Login_account.suc_name_psw))
    @unpack
    def test_01_login_success(self,username,password):
        lg = LoginPage(self.driver)
        lg.Account_password_login(username,password)
        # error_msg = lg.get_toast_error_msg()
        self.assertTrue(lg.get_element_exits())
    @data(*(Login_account.false_name_psw_notnull))
    @unpack
    def test_02_login_false(self,username,password,excpt):
        lg = LoginPage(self.driver)
        lg.Account_password_login(username, password)
        #不为空只有一个提示
        self.assertEqual(lg.get_check_error_msg(),excpt)

    @data(*(Login_account.false_name_psw_null))
    @unpack
    def test_03_login_null(self,username,password,excpt):
        lg = LoginPage(self.driver)
        lg.Account_password_login(username, password)
        # 不为空只有一个提示
        input_msg =lg.get_input_msg()
        if type(input_msg) is list:
            self.assertIn(input_msg,excpt)
        else:
            self.assertEqual(input_msg, excpt)

if __name__ == '__main__':
    unittest.main(verbosity=2)