# 163邮箱发送邮件
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# TODO 打开浏览器， 请求目标网址
driver = webdriver.Chrome()
driver.get('https://mail.163.com')

# TODO 登录操作
# 切换到登录的这个frame
frame_element = driver.find_element(By.XPATH, '//iframe[contains(@id, "x-URS-iframe")]')
driver.switch_to.frame(frame_element)

# 定位账号输入框，输入账号
time.sleep(2)
driver.find_element(By.NAME, 'email').send_keys('itsourcetest')
# 定位密码输入框，输入密码
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys('********')
# 定位登录按钮，  点击登录
time.sleep(2)
driver.find_element(By.ID, 'dologin').click()

# TODO 点击写信按钮
time.sleep(5)
# 点击信息按钮，进入写信页面
driver.find_element(By.ID, '_mail_component_149_149').click()

# TODO 写信操作
# 定位收件人，输入信息
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'nui-editableAddr-ipt').send_keys('hello@hello.com')
# 定位主 题，输入信息
time.sleep(2)
driver.find_element(By.XPATH, '//input[contains(@id, "_subjectInput")]').send_keys('test_title')
# 定位正 文，输入信息
# 切换到对应的frame中
editor_frame_element = driver.find_element(By.CLASS_NAME, 'APP-editor-iframe')
driver.switch_to.frame(editor_frame_element)

# 定位body， 输入内容
time.sleep(2)
driver.find_element(By.TAG_NAME, 'body').send_keys('content_text...')

# 切换回主页
driver.switch_to.default_content()

# 定位发送，点击操作
time.sleep(2)
driver.find_element(By.XPATH, '//footer[@class="jp0"]//span[@class="nui-btn-text"]').click()

# 退出浏览器
time.sleep(5)
driver.quit()
