from selenium import webdriver
import time
from selenium.webdriver.common.by import By
dir =webdriver.Chrome()
dir.get("https://www.baidu.com/")


#找到搜索输入框并输入字符
#search = dir.find_element(By.ID,"kw")
#search = dir.find_element_by_id("kw")


#通过name查找输入框
search = dir.find_element(By.NAME,"wd")
#search = dir.find_element_by_name("wd")

#通过类名查找输入框
search = dir.find_element(By.CLASS_NAME,"s_ipt")
#search =  dir.find_element_by_class_name("s_ipt")

#输入文本
search.send_keys("selenuim教程")

#隐性等待3秒
dir.implicitly_wait(3)

#通过xpath查找搜索按钮
searched = dir.find_element_by_xpath("//input[@class=\"bg s_btn\"]")

#点击按钮
searched.click()
time.sleep(3)
#滑动到底部
dir.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#time.sleep(6)
