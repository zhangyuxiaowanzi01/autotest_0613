from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint


class TestCase:
    def __init__(self):
        # 打开浏览器,访问百度
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def attr(self):
        # 属性定位
        # 定位 type="hidden"的标签
        elements = self.driver.find_elements(By.XPATH, '//*[@type="hidden"]')
        pprint(elements)
        print(len(elements))

    def tag_attr(self):
        # 标签定位
        # 通过 input标签定位
        elements = self.driver.find_elements(By.XPATH, '//input')
        pprint(elements)
        print(len(elements))

    def tag_index(self):
        inputs = self.driver.find_elements(By.XPATH, '//span[@class]/input[1]')
        print(inputs[0].get_attribute('outerHTML'))
        print(inputs[1].get_attribute('outerHTML'))

    def match1(self):
        # 逻辑运算符
        # 定位 name='wd' and class='s_ipt'的标签
        elements = self.driver.find_elements(By.XPATH, '//*[@name="wd" and @class="s_ipt"]')
        print(elements[0].get_attribute('outerHTML'))
        print(len(elements))

    def match2(self):
        # 模糊匹配
        # contains()  包含函数
        # text() 标签文本  <p>xxx</p>  <div>xxx</div>
        # 文本内容包含: hao
        a = self.driver.find_element(By.XPATH, '//*[contains(text(), "hao")]')
        print(a.get_attribute('outerHTML'))

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.attr()
    # case.tag_attr()
    # case.tag_index()
    # case.match1()
    case.match2()
    case.quit()
