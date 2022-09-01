from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# 打开浏览器，请求目标网址
driver = webdriver.Chrome()
url = 'file://' + os.path.join(os.path.abspath('html'), 'upload_file.html')
driver.get(url)

# 定位上传标签, 传入要上传的文件，文件必须是绝对路径
time.sleep(2)
file = os.path.join(os.path.abspath('html'), 'dog.jpeg')
driver.find_element(By.NAME, 'file').send_keys(file)

# 退出浏览器
time.sleep(5)
driver.quit()
