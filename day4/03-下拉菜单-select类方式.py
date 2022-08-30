from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome()
driver.get('https://sahitest.com/demo/selectTest.htm')

# TODO 定位要操作的select标签
s1 = driver.find_element(By.ID, 's1')
# TODO 创建Select类的实例, 传入s1对象
select = Select(s1)
# TODO 选择option选项
# 1. select.select_by_index()  通过索引选取option, 索引从0开始
time.sleep(2)
select.select_by_index(3)
# 2. select.select_by_value()  通过value值选取option
time.sleep(2)
select.select_by_value('49')
# 3. select.select_by_visible_text()  通过文本选取option
time.sleep(2)
select.select_by_visible_text('Mail')

# 退出浏览器
time.sleep(2)
driver.quit()



