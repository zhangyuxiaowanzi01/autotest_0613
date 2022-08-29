import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# 打开浏览器，访问百度
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()

# 定位元素对象
# WebElement类的实例
kw = driver.find_element(By.ID, 'kw')

# TODO 常用属性
# id标识，不是html标签属性那个id
print(kw.id)
# size, 标签在html页面中的宽高
print(kw.size)
# rect, 宽高和坐标
print(kw.rect)
# text  <span>文本内容</span>
print(kw.text)   # input是单标签，所有没有文本
# 定位新闻标签
news = driver.find_element(By.LINK_TEXT, '新闻')
print(news.text)

# TODO 常用方法
# WebElement.fn()
# 输入内容
kw.send_keys('天气预报')
time.sleep(2)
# 清空内容
# kw.clear()

# 点击
time.sleep(2)
driver.find_element(By.ID, 'su').click()


# get_attribute() 获得标签属性值的方法
time.sleep(2)
print(kw.get_attribute('outerHTML'))  # 获取标签的源码
print(kw.get_attribute('id'))
print(kw.get_attribute('name'))
print(kw.get_attribute('class'))



# 退出浏览器
# time.sleep(3)
# driver.quit()
