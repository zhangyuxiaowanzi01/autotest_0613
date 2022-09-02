import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# 显示等待定位 + EC.定位标签的方法


class Base:
    """
    selenium的二次封装，封装了selenium的基础方法，供page包下的类继承使用
    """

    def __init__(self, browser):
        # 打开浏览器，设置driver对象
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            print('不支持的浏览器')
            self.driver = None

    def get(self, url):
        # 请求目标网址
        try:
            self.driver.get(url)
        except Exception as e:
            print('无效网址')
            print(e)

    def find_element(self, locator, timeout=3):
        # 定位单个element对象
        # return webelement对象|None
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator), message='定位不到标签')
        except TimeoutException as e:
            print(e)

    def click(self, locator):
        # 元素点击操作
        element = self.find_element(locator)
        if element:
            element.click()

    def quit(self, seconds=0):
        # 退出浏览器
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    base = Base('chrome')
    base.get('https://www.baidu.com')
    # 搜索框输入天气预报
    time.sleep(2)
    kw = base.find_element((By.ID, 'kw'))
    kw.send_keys('天气预报')
    # 点击百度一下按钮
    time.sleep(2)
    base.click((By.ID, 'su'))
    # 退出浏览器
    base.quit(2)
