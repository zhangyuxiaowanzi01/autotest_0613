import time

from selenium import webdriver

# 创建options对象
options = webdriver.ChromeOptions()
# 添加无头模式参数
options.add_argument('-headless')

# 打开浏览器, 设置options对象
driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')
time.sleep(2)

# 输出百度首页的title
print(driver.title)

# 退出浏览器
driver.quit()
