from base import webdriver, By, time

# 打开浏览器， 请求目标网址
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# TODO 设置隐式等待
# 最长等待100s
driver.implicitly_wait(100)

# 定位标签
kw = driver.find_element(By.ID, 'kw')
print(kw.get_attribute('outerHTML'))

# 退出浏览器
time.sleep(2)
driver.quit()
