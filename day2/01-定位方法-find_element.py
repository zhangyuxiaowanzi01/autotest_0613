from selenium import webdriver
# TODO driver.find_element(定位类型, 类型值)
# 定位第一个匹配到的元素, 如果匹配不到抛出错误
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 定位当面页面中的第一个input元素
# input = driver.find_element(By.TAG_NAME, 'input')
# 定位页面中不存在的u标签
input = driver.find_element(By.TAG_NAME, 'u')
print(input.get_attribute('outerHTML'))

# 退出浏览器
driver.quit()


