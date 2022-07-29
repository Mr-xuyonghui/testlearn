from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class own_init():
    def __init__(self):
        self.url = "https://www.baidu.com/"
        self.brower = webdriver.Chrome()
        # self.wait = WebDriverWait(self.brower,20)
        self.brower.get(url=self.url)



if __name__ =="__main__":
    own_init()