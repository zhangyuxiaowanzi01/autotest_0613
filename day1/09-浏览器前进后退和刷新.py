from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()


# 请求百度
time.sleep(2)
driver.get('https://www.baidu.com')

# TODO 浏览器后退
time.sleep(2)
driver.back()

# TODO 浏览器前进
time.sleep(2)
driver.forward()

# TODO 浏览器刷新
time.sleep(2)
driver.refresh()

time.sleep(1)
driver.quit()





