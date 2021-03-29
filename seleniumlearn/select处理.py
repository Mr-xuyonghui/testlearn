import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumlearn import fileupload
driver = webdriver.Chrome()
driver.get("F:testlearn\seleniumlearn\select.html")
loc = (By.CLASS_NAME,"dowebok")
sel = driver.find_element(*loc)
SEL = Select(sel)
print("所有可选项：",SEL.options)
SEL.select_by_index(1)
SEL.select_by_value("three")
SEL.select_by_visible_text("two")
print("所有已选项",SEL.all_selected_options)
time.sleep(3)
SEL.deselect_by_value("three")
#针对不是select类型的选项，直接定位元素并点击即可
radio = driver.find_element_by_xpath("//input[@name=\"sex\" and @value=\"0\"]")
#选中某个选项
radio.click()
time.sleep(3)
#重复点击一个选项即取消
radio.click()

driver.find_element_by_xpath("//input[@name=\"sex\" and @value=\"1\"]").click()


#文件上传
driver.find_element_by_id("loadfile").click()
fileupload.upload("F:\testlearn\seleniumlearn\三大切换.py")