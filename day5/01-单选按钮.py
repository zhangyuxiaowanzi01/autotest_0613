from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# 打开浏览器，请求目标网址
driver = webdriver.Chrome()
url = 'file://' + os.path.join(os.path.abspath('html'), 'radio-checkbox.html')
driver.get(url)

# 单选按钮操作
# 定位标签-男 点击
time.sleep(2)
boy = driver.find_element(By.ID, 'boy')
boy.click()
# 查看按钮选中状态
print(boy.is_selected())  # True

# 定位标签-女
time.sleep(2)
gril = driver.find_element(By.ID, 'girl')
print(gril.is_selected())  # False

# 退出浏览器
time.sleep(2)
driver.quit()
