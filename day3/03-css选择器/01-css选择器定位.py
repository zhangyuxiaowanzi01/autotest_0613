import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器， 请求目标网址-百度
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 使用css选择器定位元素
# 后代选择器： E1 E2
# form input
inputs = driver.find_elements(By.CSS_SELECTOR, '#form input')
pprint(inputs)
print(len(inputs))

# 子元素选择器: E1 > E2
# form > input
inputs = driver.find_elements(By.CSS_SELECTOR, '#form>input')
pprint(inputs)
print(len(inputs))

# 并集选择器: E1, E2, E3
elements = driver.find_elements(By.CSS_SELECTOR, '#u1, #head_wrapper, #form')
pprint(elements)
print(len(elements))

# CSS[attribute="value"] 选择器
# 需求：定位type='hidden'的标签
elements = driver.find_elements(By.CSS_SELECTOR, 'input[type="hidden"]')
pprint(elements)
print(len(elements))

# nth-child()
input = driver.find_elements(By.CSS_SELECTOR, 'span input:nth-child(1)')
print(input[0].get_attribute('outerHTML'))

input = driver.find_element(By.CSS_SELECTOR, '#form input:nth-child(11)')
print(input.get_attribute('outerHTML'))

# 浏览器退出
time.sleep(2)
driver.quit()
