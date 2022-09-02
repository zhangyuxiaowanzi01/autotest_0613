from base import webdriver, By, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase:
    def __init__(self):
        # 打开浏览器， 请求目标网址
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def presence_of_element_located(self):
        # 定位标签- 显示等待
        # 在10s内，每隔0.5秒，执行一次EC.presence_of_element_located(locator)， 定位标签，直到定位到这个标签，然后返回。
        # 如果10s内，没有定位到抛出错误
        wait = WebDriverWait(self.driver, 10)
        locator = (By.ID, 'kw')
        kw = wait.until(EC.presence_of_element_located(locator), message="标签定位失败")
        print(kw.get_attribute('outerHTML'))

    def text_to_be_present_in_element(self):
        # 判断传入的locator的WebElement.text中是否包含传入值str
        # 需求： 判断hao123这个标签是否包含 hao
        wait = WebDriverWait(self.driver, 10)
        locator = (By.LINK_TEXT, 'hao123')
        result = wait.until(EC.text_to_be_present_in_element(locator, 'hello'))
        print(result)

    def quit(self):
        # 退出浏览器
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.text_to_be_present_in_element()
    case.quit()
