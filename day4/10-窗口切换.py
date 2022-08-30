import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
driver = webdriver.Chrome()
# 请求百度
driver.get('https://www.baidu.com')
# 点击新闻
time.sleep(2)
driver.find_element(By.LINK_TEXT, '新闻').click()
# 输出当前窗口标题(首页)
print(driver.title)

# 获取所有窗口的标识
window_handles = driver.window_handles
print(window_handles)
# 切换到新闻窗口
driver.switch_to.window(window_handles[1])
# 输出当前窗口标题(新闻)
print(driver.title)

# 切换到首页窗口
driver.switch_to.window(window_handles[0])
print(driver.title)

# 退出浏览器
time.sleep(2)
driver.quit()
