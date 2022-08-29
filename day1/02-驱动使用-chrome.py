# 导入selenium
from selenium import webdriver
import time

# TODO 打开浏览器-chrome浏览器
# 打开chrome浏览器,返回驱动对象
driver = webdriver.Chrome()
time.sleep(2)


# TODO 退出浏览器
driver.quit()
