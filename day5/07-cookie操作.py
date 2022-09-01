from base import webdriver, os, time, By
from pprint import pprint

# 打开浏览器，请求目标网址
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 操作cookie
# driver.get_cookies()	获得所有cookie 信息
# pprint(driver.get_cookies())

# driver.get_cookie(name)	返回特定name 的cookie 信息
# print(driver.get_cookie('BAIDUID_BFESS'))

# driver.add_cookie(cookie_dict)	添加cookie，必须有name 和value 值
driver.add_cookie({'name': 'hello', 'value': '11111111111111111'})
pprint(driver.get_cookies())

# driver.delete_cookie(name)	删除特定(部分)的cookie 信息
driver.delete_cookie('hello')
pprint(driver.get_cookies())

# driver.delete_all_cookies()	删除所有cookie 信息
driver.delete_all_cookies()
print(driver.get_cookies())

# 退出浏览器
time.sleep(2)
driver.quit()
