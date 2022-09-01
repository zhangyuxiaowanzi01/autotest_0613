import time
from selenium import webdriver

# 打开浏览器， 请求目标网址
driver = webdriver.Chrome()
driver.get('https://mail.qq.com')

# 退出浏览器
time.sleep(5)
driver.quit()
