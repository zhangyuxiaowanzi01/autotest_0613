import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器, 请求目标网址:源码
driver = webdriver.Chrome()
driver.get('https://www.itsource.cn/')

# 定位弹窗的关闭按钮,然后点击
time.sleep(3)
span = driver.find_element(By.XPATH, '//span[@onclick="hide_floatWindow();"]')
span.click()

# 退出浏览器
time.sleep(5)
driver.quit()