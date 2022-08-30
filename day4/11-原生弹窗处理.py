from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome()
url = 'file://' + os.path.join(os.path.abspath('html'), 'popup.html')
driver.get(url)

# 定位所有button
btns = driver.find_elements(By.TAG_NAME, 'button')
# TODO alert
time.sleep(2)
btns[0].click()
# 切换到弹窗
alter = driver.switch_to.alert
# 弹窗描述信息
print(alter.text)
# 弹窗确认
time.sleep(2)
alter.accept()


# TODO confirm
time.sleep(2)
btns[1].click()
confirm = driver.switch_to.alert
# 弹窗描述信息
print(confirm.text)
# 弹窗取消
time.sleep(2)
confirm.dismiss()

# TODO prompt
time.sleep(2)
btns[2].click()
prompt = driver.switch_to.alert
# 弹窗描述信息
print(prompt.text)
# 弹窗输入内容
time.sleep(1)
prompt.send_keys('hello selenium')
# 弹窗确定
time.sleep(2)
prompt.accept()


# 退出浏览器
time.sleep(5)
driver.quit()