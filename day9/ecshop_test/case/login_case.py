import time
import unittest
import ddt
from common.base import get_driver
from page.login_page import LoginPage
from page.index_page import IndexPage
from common.data_operation import DataOperation

account_list = DataOperation('account.csv').get_data_to_dict()
account_list2 = []
for account in account_list:
    try:
        account['password'] = int(account['password'])
    except ValueError:
        account['password'] = 0
    account_list2.append(account)

print(account_list2)


@ddt.ddt
class LoginCase(unittest.TestCase):
    account_list = account_list

    @classmethod
    def setUpClass(cls) -> None:
        # 打开浏览器
        driver = get_driver()
        cls.login = LoginPage(driver)
        cls.index = IndexPage(driver)

    @ddt.data(*account_list)
    def test_login(self, data):
        username = data.get('username')
        password = data.get('password')

        # 请求目标网址
        self.login.get(self.login.login_url)
        self.login.implicitly_wait()

        # 登录操作
        self.login.input_username(username)
        self.login.input_password(password)
        self.login.input_remember()
        self.login.input_submit()

        # 断言 左上角用户名和登录的用户名相同
        # 预期数据 和 实际数据 比对
        login_username = self.index.font_text()
        self.assertEqual(username, login_username)

    def tearDown(self) -> None:
        # 退出登录
        self.index.a_link()

    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭浏览器
        cls.login.quit(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
