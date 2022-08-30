from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 打开浏览器
driver = webdriver.Chrome()
# 请求百度首页
time.sleep(1)
driver.get('https://www.baidu.com')

# 在搜索框输入天气预报
time.sleep(1)
kw = driver.find_element(By.ID, 'kw')
kw.send_keys('天气预报')


# TODO 键盘操作: 全选搜索框中的内容
time.sleep(2)
kw.send_keys(Keys.CONTROL, 'a')

# TODO 键盘操作:复制选中的内容
time.sleep(2)
kw.send_keys(Keys.CONTROL, 'c')

# 请求360搜索
driver.get('https://www.so.com')
# TODO 键盘操作:将复制的内容粘贴到搜索框中
time.sleep(2)
driver.find_element(By.ID, 'input').send_keys(Keys.CONTROL, 'v')

# 点击搜索
time.sleep(2)
driver.find_element(By.ID, 'search-button').click()

# 退出浏览器
time.sleep(2)
driver.quit()