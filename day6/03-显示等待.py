from base import webdriver, By, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 打开浏览器， 请求目标网址
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# until 检测百度首页的title是 'xxx'
"""
# until: 等待True， 超时没有返回True， 就抛出异常。
# 创建wait对象
wait = WebDriverWait(driver, 20)
result1 = wait.until(EC.title_is('百度一下，你就知道1'), message='标题不一致')
print(result1)
# selenium.common.exceptions.TimeoutException: Message: 标题不一致
"""

# until_not: 检测百度首页的title不是 'xxx'
# 等待False， 超时没有返回False，就抛出异常
wait = WebDriverWait(driver, 10)
result2 = wait.until_not(EC.title_is('百度一下，你就知道'), message='标题一致')
print(result2)

# 退出浏览器
time.sleep(2)
driver.quit()
