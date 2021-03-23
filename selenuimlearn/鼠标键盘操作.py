from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://res.youcheyihou.com/test/node/auto_home_pc/")
loc = (By.LINK_TEXT,"选车")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
handles = driver.window_handles
driver.switch_to.window(handles[-1])
#显性等待新的窗口打开
WebDriverWait(driver,10).until(EC.new_window_is_opened)
loc2 = (By.XPATH,"//span[text()=\"自主\"]//preceding-sibling::span")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc2))
driver.find_element(*loc2).click()


# #实例化
# select = Select()
# # driver.find_element(By.XPATH)
loc3 = (By.XPATH,"//input[@placeholder=\"轿车\"]")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc3))
driver.find_element(*loc3).click()
driver.find_element(By.XPATH,"//span[text()=\"小型车\"]/parent::li").click()

driver.find_element_by_xpath("//div[@class=\"el-select__tags\"][1]").click()

