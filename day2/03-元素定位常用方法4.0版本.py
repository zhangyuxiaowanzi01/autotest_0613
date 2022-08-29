from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase:
    def __init__(self):
        # 打开浏览器,返回驱动对象
        self.driver = webdriver.Chrome()
        # 访问百度
        self.driver.get('https://www.baidu.com')

    def id(self):
        # 通过id来定位元素
        # <webElement>
        kw = self.driver.find_element(By.ID, 'kw')
        # 获取标签属性 web_element.get_attribute('outerHTML')
        # outerHTML: 获取这个标签对象对应的html内容
        print(kw.get_attribute('outerHTML'))

    def class_name(self):
        s_ipt = self.driver.find_element(By.CLASS_NAME, 's_ipt')
        print(s_ipt.get_attribute('outerHTML'))

    def link_text(self):
        # 通过a标签的文本定位元素
        map_obj = self.driver.find_element(By.LINK_TEXT, '地图')
        print(map_obj.get_attribute('outerHTML'))

        # 定位图片这个a链接
        image1 = self.driver.find_element(By.LINK_TEXT, '图片')
        print(image1.get_attribute('outerHTML'))

        # 定位图片这个a链接
        image2 = self.driver.find_element(By.PARTIAL_LINK_TEXT, '图片')
        print(image2.get_attribute('outerHTML'))

    def partial_link_text(self):
        # 通过部分链接文本来定位元素
        hao = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'hao')
        print(hao.get_attribute('outerHTML'))

    def name(self):
        # 通过name属性来定位标签
        wd = self.driver.find_element(By.NAME, 'wd')
        print(wd.get_attribute('outerHTML'))

    def tag_name(self):
        # 通过标签名称(html标签名)来定位元素
        print(self.driver.find_element(By.TAG_NAME, 'form').get_attribute('outerHTML'))

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()

    # case.id() # 通过id获取
    # case.class_name()  # 通过class获取
    case.link_text()  # 通过链接文本定位标签
    # case.partial_link_text() # 通过部分文本链接定位标签
    # case.name()  # 通过name属性来定位标签
    # case.tag_name()  # 通过标签名称(html标签名)来定位元素
    case.quit()
