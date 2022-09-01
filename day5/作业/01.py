# 注册页面练习
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


class TestCase:
    def __init__(self):
        # 打开浏览器，创建driver对象
        self.driver = webdriver.Chrome()
        # 请求目标网址
        local_url = 'file://' + os.path.join(os.path.abspath('html'), '注册实例.html')
        self.driver.get(local_url)

    def default_content(self):
        # TODO 操作主页面的表单
        # 账号输入内容
        time.sleep(2)
        self.driver.find_element(By.ID, 'user').send_keys('hello')

        # 点击注册用户
        time.sleep(2)
        self.driver.find_element(By.TAG_NAME, 'button').click()

        # 点击新浪链接
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, '访问 新浪 网站').click()

        # 下拉框选择重庆
        # 1定位select标签
        select_element = self.driver.find_element(By.ID, 'select')
        # 2创建select对象
        select = Select(select_element)
        # 3选择option-有3种选择option的方式
        select.select_by_index(3)

        # 操作alert
        time.sleep(2)
        self.driver.find_element(By.ID, 'alert').click()

        # 处理弹窗
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()

    def page_a(self):
        # TODO 操作注册用户A frame的表单
        # 从主页切换到 a frame
        time.sleep(2)
        self.driver.switch_to.frame('idframe1')

        # 定位一个标签，证明切换成功
        legend = self.driver.find_element(By.TAG_NAME, 'legend')
        print(legend.get_attribute('outerHTML'))

    def page_b(self):
        # TODO 操作注册用户B frame的表单
        # 从 a frame 切换到 b frame
        # 1. 从aframe切换到主页
        self.driver.switch_to.default_content()
        # 2. 从主页切换到b frame
        self.driver.switch_to.frame('/html/body/s/iframe[2]')

        # 定位一个标签，证明切换成功
        legend = self.driver.find_element(By.TAG_NAME, 'legend')
        print(legend.get_attribute('outerHTML'))

    def quit(self):
        # 退出浏览器
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.default_content()
    case.page_a()
    case.page_b()
    case.quit()
