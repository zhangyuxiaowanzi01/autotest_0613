import time

from selenium import webdriver

# 打开浏览器, 访问百度
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# xpath方式定位
# 搜索框输入天气预报
time.sleep(2)
driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys('天气预报')

# 点击搜索框按钮
time.sleep(2)
driver.find_element(By.XPATH, '//input[@value="百度一下"]').click()


# 退出浏览器
time.sleep(2)
driver.quit()

