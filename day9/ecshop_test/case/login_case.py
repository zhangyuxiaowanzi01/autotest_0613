import unittest
from common.base import get_driver
from page.login_page import LoginPage
from page.index_page import IndexPage


class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 打开浏览器
        driver = get_driver()
        cls.login = LoginPage(driver)
        cls.index = IndexPage(driver)

    def test_login(self):
        # 请求目标网址
        self.login.get('https://ecshop.test2.shopex123.com/user.php')
        self.login.implicitly_wait()

        # 登录操作
        self.login.input_username('fine1')
        self.login.input_password('123456')
        self.login.input_remember()
        self.login.input_submit()

        # 断言 左上角用户名和登录的用户名相同
        # 预期数据 和 实际数据 比对
        login_username = self.index.font_text()
        self.assertEqual('fine1', login_username)

    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭浏览器
        cls.login.quit(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
