from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

# TODO driver.find_elements(定位类型, 类型值)
# 定位所有匹配到标签, 返回列表, 定位不到返回空列表

# 打开浏览器, 访问百度
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 定位input标签
# find_elements(By.TAG_NAME, 类型值)
# inputs = driver.find_elements(By.TAG_NAME, 'input')
# 定位在页面中不存在的u标签
inputs = driver.find_elements(By.TAG_NAME, 'u')
pprint(inputs)
print(len(inputs))

# 退出浏览器
driver.quit()
