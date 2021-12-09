import time

from selenium.webdriver.remote.webdriver import WebDriver
from seleniumlearn.PageLocators import LoginLoctors as locs
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class LoginPage:
    #声明对象类型，实现代码提示
    def __init__(self,driver:WebDriver):
        #初始化driver
        self.driver = driver
    def Account_password_login(self,username,password):
        #输入账号密码
        WebDriverWait(self.driver, 10).until(ec.new_window_is_opened)
        login_model = self.driver.find_element(*locs.login_model).text
        if login_model == "账号密码登录":
            WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locs.login_model), "查找元素超时")
            self.driver.find_element(*locs.change_model).click()
            self.driver.find_element(*locs.user_input).send_keys(username)
            self.driver.find_element(*locs.psw_input).send_keys(password)
            self.driver.find_element(*locs.login_button).click()
            self.driver.implicitly_wait(20)
        else:
            self.driver.find_element(*locs.user_input).send_keys(username)
            self.driver.find_element(*locs.psw_input).send_keys(password)
            time.sleep(4)
            self.driver.find_element(*locs.login_button).click()
    # def get_toast_error_msg(self):
    #     return self.driver.find_element(*locs.toast_error_msg).text

    def get_check_error_msg(self):
        eles = self.driver.find_elements(*locs.check_error_msg)
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) >1:
            text_list =[]
            for ele in eles:
                text_list.append(ele.text)
            return text_list
    def get_element_exits(self):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(*locs.login_suc))
        except:
            return False
        else:
            return True
    def get_input_msg(self):
        #return self.driver.find_element(*locs.input_msg).text
        eles = self.driver.find_elements(*locs.input_msg)
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) > 1:
            text_list = []
            for ele in eles:
                text_list.append(ele.text)


