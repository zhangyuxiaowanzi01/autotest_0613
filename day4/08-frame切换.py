from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome()
url = 'file://' + os.path.join(os.path.abspath('html'), 'frame.html')
driver.get(url)

# 定位标签
time.sleep(2)
# <h3>frame</h3>
h3 = driver.find_element(By.TAG_NAME, 'h3')
print(h3.get_attribute('outerHTML'))

# TODO 切换到<iframe id="f1" src="inner.html"  name="inner">
# frame的id
# driver.switch_to.frame('f1')
# frame的name
# driver.switch_to.frame('inner')
# frame的webelement对象
inner = driver.find_element(By.ID, 'f1')
driver.switch_to.frame(inner)

# <h3 id="inner_h3">inner</h3>
inner_h3 = driver.find_element(By.ID, 'inner_h3')
print(inner_h3.get_attribute('outerHTML'))

# <iframe id="f2">
driver.switch_to.frame('f2')
time.sleep(2)
print(driver.find_element(By.ID, 'p1').get_attribute('outerHTML'))


# TODO 切换到父级frame
driver.switch_to.parent_frame()
print(driver.find_element(By.ID, 'inner_h3').get_attribute('outerHTML'))


# TODO 切换到主页面
# 说明:不管当前在哪个frame, 使用这个方法都会切换到主页面
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, 'h3').get_attribute('outerHTML'))

# 退出浏览器
time.sleep(2)
driver.quit()