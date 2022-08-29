# 导入selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器，请求目标网址（demo.html）
driver = webdriver.Chrome()
driver.get('file:///Users/fine/teach/itsouce/autotest_0613/day3/%E4%BD%9C%E4%B8%9A/demo.html')

# 标签名定位-h1
h1 = driver.find_element(By.TAG_NAME, 'h1')
print(h1.get_attribute('outerHTML'))

# id定位方式
id_dragger = driver.find_element(By.ID, 'dragger')
print(id_dragger.get_attribute('outerHTML'))

# xpath定位-div[@class=itemX]
divs = driver.find_elements(By.XPATH, '//div[@class]')
for div in divs:
    print(div.get_attribute('outerHTML'))

# xpath定位-p[@class]
p = driver.find_element(By.XPATH, '//p[@class]')
print(p.get_attribute('outerHTML'))


# div-sub1这个div
div = driver.find_element(By.XPATH, '//div[@id="div1"]/div[1]')
print(div.get_attribute('outerHTML'))

# div-sub1这个div
div = driver.find_element(By.XPATH, '//div[@id="div1"]/div[2]')
print(div.get_attribute('outerHTML'))

# xpath - span1
span1 = driver.find_element(By.XPATH, '//span')
print(span1.get_attribute('outerHTML'))

# xpath - span2
span2 = driver.find_element(By.XPATH, '//p[@class="p2"]/span')
print(span2.get_attribute('outerHTML'))

# 退出浏览器
time.sleep(2)
driver.quit()