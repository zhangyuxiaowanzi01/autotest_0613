from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 1、打开Chrome，打开百度首页
driver = webdriver.Chrome()
time.sleep(2)

# TODO 请求网址-百度
driver.get('https://www.baidu.com')
time.sleep(2)

# 2、搜索框输入 "天气预报"，点击百度一下
# TODO 元素定位 driver.find_element(定位方式, 定位的值)
kw = driver.find_element(By.ID, 'kw')
# TODO 表单域输入内容
kw.send_keys('天气预报')
time.sleep(2)

# 元素定位 - 定位百度一下按钮
su = driver.find_element(By.ID, 'su')
# TODO 点击方法
su.click()
# 3、等待2秒
time.sleep(2)

# 4、TODO 获取页面标题，并打印出来
title = driver.title
print(title)

# 5、检查’天气’关键字是否在标题中
if '天气' in title:
    print('ok')
else:
    print('no')

# 6、关闭Chrome浏览器
driver.quit()