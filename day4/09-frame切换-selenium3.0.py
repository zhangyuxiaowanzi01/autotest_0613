from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome()
url = 'file://' + os.path.join(os.path.abspath('html'), 'frame.html')
driver.get(url)

# 切换iframe: f1
driver.switch_to_frame('f1')
h3 = driver.find_element_by_tag_name('h3')
print(h3.get_attribute('outerHTML'))

# 退出浏览器
driver.quit()

