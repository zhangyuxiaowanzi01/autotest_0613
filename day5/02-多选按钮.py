from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# 打开浏览器，请求目标网址
driver = webdriver.Chrome()
url = 'file://' + os.path.join(os.path.abspath('html'), 'radio-checkbox.html')
driver.get(url)

# 多选按钮操作
# 全部选中
input_list = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
# 遍历列表，点击里面的元素-选中
for input_element in input_list:
    time.sleep(2)
    input_element.click()
    print(input_element.is_selected())

# 遍历列表，点击里面的元素-选中
for input_element in input_list:
    time.sleep(2)
    input_element.click()
    print(input_element.is_selected())

# 退出浏览器
time.sleep(2)
driver.quit()
