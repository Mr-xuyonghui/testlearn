from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index")
WebDriverWait(driver,5).until(ec.new_window_is_opened)
mdd = driver.find_element_by_id("HD_CityName")
mdd.send_keys("上海")
# #目的地输入
query = """
var mdd = document.getElementById("HD_CityName");
mdd.setAttribute("_lastvalue","上海")
var cityid = document.getElementById("HD_CityId");
cityid.value= 2;
var citypy = document.getElementById("HD_CityPy");
citypy.value = "Shanghai";
//有的需要移除readonly属性，removeAttribute("readonly")
var datein = document.getElementById("HD_CheckIn");
datein.value = "2021-04-29";
var dateout = document.getElementById("HD_CheckOut")
dateout.value = "2021-05-04"
"""
driver.execute_script(query)
people = driver.find_element_by_id("J_roomCountList")
#实例化select
sel =Select(people)
sel.select_by_index(4)
a=sel.all_selected_options
peoplecut = a[0].get_attribute("value")
crs = 5
ets =2
etn =1,2
query_1 ="""
var peoplecunt = document.getElementById("J_RoomGuestInfoTxt");
peoplecunt.removeAttribute("readonly")
var totalc =document.getElementById("J_RoomGuestCount")
//未进行联动
totalc.value="5,5,2,1,2"
"""
driver.execute_script(query_1,peoplecut,crs,ets,etn)
totalpeople = driver.find_element_by_id("J_RoomGuestInfoTxt")
totalpeople.clear()
totalpeople.send_keys(str(peoplecut)+"成人"+str(ets)+"儿童")

driver.find_element_by_id("HD_Btn").click()



