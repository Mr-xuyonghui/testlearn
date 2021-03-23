import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as  ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
WebDriverWait(driver,10).until(ec.new_window_is_opened)
loc = (By.ID,"s-usersetting-top")
setting =driver.find_element(*loc)
actionc = ActionChains(driver)
actionc.move_to_element(setting)
#执行鼠标操作
actionc.perform()
loc2 = (By.XPATH,"//div[@id=\"s-user-setting-menu\"]//a[text()=\"高级搜索\"]")
WebDriverWait(driver,10).until(ec.visibility_of_element_located(loc2))
driver.find_element(*loc2).click()
loc_set = (By.XPATH,"//ul[@class=\"pftab_hd\"]/li[text()=\"搜索设置\"]")
WebDriverWait(driver,10).until(ec.visibility_of_element_located(loc_set))
souset=driver.find_element(By.XPATH,"//ul[@class=\"pftab_hd\"]/li[text()=\"搜索设置\"]")
if souset.get_attribute("class") == "item cur":
    #弹窗中切换到搜索设置
    driver.find_element(By.XPATH,"//li[text()=\"搜索设置\"]").click()
    #进行系列测试并
    driver.find_element(By.XPATH,"//label[@for=\"s1_2\"]").click()
    driver.find_element(By.XPATH,"//label[@for=\"SL_1\"]").click()
    driver.find_element(By.XPATH,"//label[@for=\"nr_3\"]").click()
    time.sleep(3)
    driver.find_element_by_link_text("保存设置").click()
    driver.switch_to.alert.accept()
else:
    driver.find_element_by_xpath("//span[text()=\"包含任意关键词\"]//following-sibling::input").send_keys("教程")
    driver.find_element_by_xpath("//label[@for=\"q5_1\"]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id=\"adv-setting-8\"]/input").click()
    WebDriverWait(driver,20).until(ec.new_window_is_opened)
    driver.find_element(By.ID,"kw").send_keys("教程")
    time.sleep(3)
    driver.find_element(By.ID, "kw").send_keys(Keys.BACK_SPACE)




