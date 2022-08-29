import time

from selenium import webdriver

# 创建options对象
options = webdriver.ChromeOptions()
# 为options对象添加手机配置
mobileEmulation = {"deviceName": 'iPhone 6'}
options.add_experimental_option('mobileEmulation', mobileEmulation)


# 打开浏览器,添加配置项
driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')
time.sleep(3)

# 退出浏览器
driver.quit()