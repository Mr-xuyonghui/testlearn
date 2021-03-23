from more_itertools import last
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

dir =webdriver.Chrome()
dir.get("https://www.baidu.com/")

#找到搜索输入框并输入字符
search = dir.find_element(By.ID,"kw")
search.send_keys("selenuim教程")
#通过xpath查找搜索按钮
searched = dir.find_element_by_xpath("//input[@class=\"bg s_btn\"]")
#点击按钮
searched.click()
#隐性等待五秒
#dir.implicitly_wait(5)
loc = (By.LINK_TEXT,"selenium webdriver 使用教程 - 简书")
WebDriverWait(dir,10).until(EC.visibility_of_element_located(loc))

clickele = dir.find_element(By.LINK_TEXT,"selenium webdriver 使用教程 - 简书")
clickele.click()
print("所有句柄:"+str(dir.window_handles))

handles = dir.window_handles
print("切换前当前句柄"+dir.current_window_handle)
dir.switch_to_window(handles[-1])
print("切换后当前句柄"+dir.current_window_handle)
lod2 =(By.XPATH,"//nav[@class=\"_3JYrtj\"]/a[1]")

WebDriverWait(dir,5).until(EC.visibility_of_element_located(lod2))
dir.find_element(By.XPATH,"//nav[@class=\"_3JYrtj\"]/a[1]").click()




