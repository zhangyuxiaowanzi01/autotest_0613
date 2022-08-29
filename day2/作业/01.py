# 完成上课demo的案例
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    def __init__(self):
        self.__driver = webdriver.Chrome()

    def get_so(self, keyword):
        # 访问网址-so.com
        time.sleep(2)
        self.__driver.get('https://www.so.com')
        # 定位搜索框, 输入关键字
        time.sleep(2)
        self.__driver.find_element(By.ID, 'input').send_keys(keyword)
        # 定位搜索按钮,点击
        time.sleep(2)
        self.__driver.find_element(By.ID, 'search-button').click()

    def quit(self):
        time.sleep(2)
        self.__driver.quit()


if __name__ == '__main__':
    # 第一种
    # TestDemo().get_so('天气预报')
    # TestDemo().quit()

    # 第二种
    test_demo = TestDemo()
    test_demo.get_so('天气预报')
    test_demo.quit()
