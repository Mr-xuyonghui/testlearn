import unittest
from selenium import webdriver
import time
class Test_ready(unittest.TestCase):
    def __init__(self,url):
        super().__init__()
        self.url = url

    def setUp(self) -> None:
        print("测试前准备开始")
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

test_rea=Test_ready('https://www.zhihu.com/signin?next=%2F')