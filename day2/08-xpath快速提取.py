from selenium import webdriver

# 打开浏览器, 访问百度
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# xpath定位搜索框
print(driver.find_element('xpath', '//*[@id="kw"]').get_attribute('outerHTML'))
