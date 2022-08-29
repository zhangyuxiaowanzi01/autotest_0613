import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器，返回webdriver对象
# driver: Webdriver的实例对象
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# print(driver)

# 打开新闻页面
# 定位新闻标签
time.sleep(1)
driver.find_element(By.LINK_TEXT, '新闻').click()

# TODO 常用属性
# 浏览器名称
# print(driver.name)
# 当前url
# print(driver.current_url)
# 当前页面标题
# print(driver.title)
# 网页源码
# print(driver.page_source)


# 当前浏览器的所有窗口句柄
# 后面用来切换窗口用的
print(driver.window_handles)
# 当前窗口句柄
print(driver.current_window_handle)

# 退出浏览器
time.sleep(10)
driver.close()
