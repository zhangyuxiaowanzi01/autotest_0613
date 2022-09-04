# 每个测试页面，对应page包下的一个模块,每个模块下定义一个页面类
"""
测试需求：
在输入框中输入关键字
点击百度一下按钮
"""
from common.base import Base, By, get_driver, time


class IndexPage(Base):
    """
    页面元素的定位和操作
    """

    def input_text(self, keyword):
        # 输入框中输入关键字
        self.send_keys((By.ID, 'kw'), keyword)

    def input_button(self):
        # 点击百度一下按钮
        self.click((By.ID, 'su'))


if __name__ == '__main__':
    # 创建driver对象
    driver = get_driver()
    index = IndexPage(driver)
    # 访问目标网址
    index.get('https://www.baidu.com')
    index.implicitly_wait()  # 隐式等待

    # 操作
    time.sleep(2)
    index.input_text('天气预报')  # 输入天气预报

    time.sleep(2)
    index.input_button()   # 点击百度一下

    # 退出浏览器
    index.quit(5)
