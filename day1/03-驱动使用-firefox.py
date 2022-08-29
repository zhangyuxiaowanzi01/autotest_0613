# 导入selenium
from selenium import webdriver
import time

# TODO 打开浏览器-firefox
# 打开浏览器, 返回浏览器驱动
driver = webdriver.Firefox()
time.sleep(2)

# TODO 退出浏览器
driver.quit()