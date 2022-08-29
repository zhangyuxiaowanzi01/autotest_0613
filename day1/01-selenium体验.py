from selenium import webdriver

from selenium.webdriver.common.by import By
import time

# 打开chrome浏览器
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()


# 在浏览器中输入网址-www.baidu.com
driver.get('http://www.baidu.com')
time.sleep(2)

# 在搜索框中输入"天气预报"
kw = driver.find_element(By.ID, 'kw')
kw.send_keys('天气预报')
time.sleep(2)

# 点击百度一下按钮
su = driver.find_element(By.ID, 'su')
su.click()
time.sleep(2)

# 关闭浏览器
driver.quit()