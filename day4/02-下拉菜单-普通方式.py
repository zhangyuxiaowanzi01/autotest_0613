from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器,访问目标网址
driver = webdriver.Chrome()
driver.get('https://sahitest.com/demo/selectTest.htm')

# 定位下拉框标签 select: id='s1'  [建议使用这种]
time.sleep(2)
select = driver.find_element(By.ID, 's1')
# 通过下拉框标签定位要选择的选项标签 : Email, 点击
option = select.find_element(By.CSS_SELECTOR, 'option[value="48"]')
option.click()

# 定位下拉框标签: select id="s3Id"
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'option[value="o4val"]').click()

# 退出浏览器
time.sleep(2)
driver.quit()

