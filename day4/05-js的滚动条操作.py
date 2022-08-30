from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
# 搜索框输入天气预报
time.sleep(2)
driver.find_element(By.ID, 'kw').send_keys('天气预报')
# 点击百度一下的按钮
time.sleep(2)
driver.find_element(By.ID, 'su').click()

# TODO 滚动条操作
# 滚动到页面的最底部
time.sleep(2)
js1 = 'window.scrollTo(0, document.body.scrollHeight)'
driver.execute_script(js1)

# 滚动到页面的最顶部
time.sleep(3)
js2 = 'window.scrollTo(0, 0)'
driver.execute_script(js2)


# 退出浏览器
time.sleep(10)
driver.quit()