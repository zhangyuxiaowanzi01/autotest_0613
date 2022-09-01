import time
from selenium import webdriver

# 设置options对象，添加个人路径参数到配置对象
options = webdriver.ChromeOptions()
user_data_dir = r'--user-data-dir=/Users/fine/Library/Application Support/Google/Chrome'
options.add_argument(user_data_dir)

# 打开浏览器， 请求目标网址
time.sleep(2)
driver = webdriver.Chrome(options=options)
driver.get('https://mail.163.com')

# 退出浏览器
time.sleep(2)
driver.quit()
