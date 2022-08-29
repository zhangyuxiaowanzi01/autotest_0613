from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 打开浏览器
driver = webdriver.Chrome()

# 访问百度
time.sleep(2)
driver.get('https://www.baidu.com')

# 点击新闻按钮-获取新闻标签,点击
time.sleep(2)
driver.find_element(By.LINK_TEXT, '新闻').click()

# 关闭当前窗口
time.sleep(2)
driver.close()

# 退出浏览器
time.sleep(2)
driver.quit()

