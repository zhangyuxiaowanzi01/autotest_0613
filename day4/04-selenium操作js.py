from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# TODO 执行js代码
time.sleep(2)
js = 'alert("居家快乐")'
driver.execute_script(js)

# 退出浏览器
time.sleep(2)
driver.quit()

