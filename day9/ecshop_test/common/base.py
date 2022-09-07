import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# 获取driver对象
def get_driver(browser='chrome'):
    # 打开浏览器，返回driver
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        print('不支持的浏览器')

    # 浏览器最大化
    if driver:
        driver.maximize_window()

    return driver


class Base:
    """
    selenium的二次封装，封装了selenium的基础方法，供page包下的类继承使用
    """

    def __init__(self, driver):
        # 设置driver
        self.driver = driver

    def get(self, url):
        # 请求目标网址
        try:
            self.driver.get(url)
        except Exception as e:
            print('无效网址')
            print(e)

    def find_element(self, locator, timeout=1):
        # 定位单个element对象
        # return web_element对象|None
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            print('定位不到标签')

    def find_elements(self, locator, timeout=1):
        # 定位多个element对象
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_all_elements_located(locator), message='定位不到标签')
        except TimeoutException as e:
            print('定位不到标签')
            return []

    def clear(self, locator):
        # 输入框清空内容
        element = self.find_element(locator)
        if element:
            element.clear()

    def get_attribute(self, locator, attr_name):
        # 获取元素属性
        element = self.find_element(locator)
        if element:
            return element.get_attribute(attr_name)

    def send_keys(self, locator, content):
        # 输入框输入内容
        element = self.find_element(locator)
        if element:
            element.send_keys(content)

    def click(self, locator):
        # 元素点击操作
        element = self.find_element(locator)
        if element:
            element.click()

    def implicitly_wait(self, seconds=3):
        # 隐式等待
        self.driver.implicitly_wait(seconds)

    def get_element_text(self, locator):
        # 获取标签文本
        element = self.find_element(locator)
        if element:
            return element.text

    def quit(self, seconds=0):
        # 退出浏览器
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    driver_obj = get_driver()

    base = Base(driver_obj)
    base.get('https://www.baidu.com')

    # news = base.find_element((By.LINK_TEXT, '新闻'))
    # print(news.text)
    print(base.get_element_text((By.LINK_TEXT, '新闻')))

    # 搜索框输入天气预报
    time.sleep(2)
    kw = base.find_element((By.ID, 'kw'))

    time.sleep(1)
    base.send_keys((By.ID, 'kw'), '天气预报')

    time.sleep(1)
    base.clear((By.ID, 'kw'))

    time.sleep(1)
    print(base.get_attribute((By.ID, 'kw'), 'outerHTML'))

    # 退出浏览器
    base.quit(2)
