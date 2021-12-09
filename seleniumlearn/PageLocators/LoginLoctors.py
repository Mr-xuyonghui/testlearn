from selenium.webdriver.common.by import By

#登录模式
login_model = (By.XPATH,'//div[@class="login-title"]')
#账号输入框
user_input = (By.XPATH,'//input[@name="username"]')
#密码输入框
psw_input = (By.XPATH,'//input[@name="password"]')
#记住密码
#el-checkbox__input is-checked为选中
rem_psw = (By.XPATH,'//span[@class="el-checkbox__label"]//ancestor::label/span[1]')
#忘记密码
forget_psw = (By.XPATH,'//span[@class="login-error-text"]')
#登录按钮
login_button = (By.XPATH,'//div[@class="login-button"]')
#切换登录模式
change_model= (By.XPATH,'//div[@class="flex justify-content-between other-login"]/div/button')
# #错误提示:Server: 帐号或者密码错误----隐藏之后不可见，定位不到 不可用
# toast_error_msg = (By.XPATH,'//p[@class="el-message__content"]')
#检查错误提示-请输入正确的账号密码
check_error_msg = (By.XPATH,'//span[@class="check-submit-point"]')
#输入框错误实体
input_msg = (By.XPATH,'//span[@class="login-point"]')
#登录成功退出按钮
login_suc = (By.XPATH,'//span[text()="退出"]')