from selenium import webdriver

# 打开浏览器, 访问test.html
driver = webdriver.Chrome()
driver.get('file:///E:/20220613%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E7%B2%BE%E8%8B%B1%E7%8F%AD/autotest_0613/day2/html/test.html')

# div标签
# //p/following-sibling::div
elements = driver.find_elements('xpath', '//p/following-sibling::div')
print(elements[0].get_attribute('outerHTML'))


elements = driver.find_elements('xpath', '//p/preceding-sibling::div')
print(elements[0].get_attribute('outerHTML'))

driver.quit()
