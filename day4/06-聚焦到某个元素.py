from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.163.com/')

# 定位元素: 163
time.sleep(2)
target = driver.find_element(By.LINK_TEXT, '财经')

# TODO 聚焦到某个标签
time.sleep(1)
js = 'arguments[0].scrollIntoView()'
driver.execute_script(js, target)

# 退出浏览器
time.sleep(8)
driver.quit()

