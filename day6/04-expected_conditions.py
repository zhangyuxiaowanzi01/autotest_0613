from base import webdriver, By, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 打开浏览器， 请求目标网址
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 定位标签- 显示等待
# 在10s内，每隔0.5秒，执行一次EC.presence_of_element_located(locator)， 定位标签，直到定位到这个标签，然后返回。
# 如果10s内，没有定位到抛出错误
wait = WebDriverWait(driver, 10)
locator = (By.ID, 'kw')
kw = wait.until(EC.presence_of_element_located(locator), message="标签定位失败")
print(kw.get_attribute('outerHTML'))

# 退出浏览器
time.sleep(2)
driver.quit()



