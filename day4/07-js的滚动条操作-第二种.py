from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.163.com/')


# TODO 滚动条操作
# 滚动到页面的最底部
time.sleep(2)
# js对象: {}
# js数组: []
js1 = 'window.scrollTo({left:0, top:document.body.scrollHeight, behavior:"smooth"})'
driver.execute_script(js1)

# 滚动到页面的最顶部
time.sleep(3)
js2 = 'window.scrollTo(0, 0)'
driver.execute_script(js2)

# 退出浏览器
time.sleep(10)
driver.quit()