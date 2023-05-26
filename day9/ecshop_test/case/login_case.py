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
    """
    读取csv格式中的数据对数据进行分析,使用数据驱动自动化执行
    """
    try:
        account['password'] = int(account['password'])
    except ValueError:
        account['password'] = 0
    account_list2.append(account)

print(account_list2)


@ddt.ddt
#  使用数据驱动ddt中的ddt模块(系统自带的优先级,响应速度都是比较高的)
class LoginCase(unittest.TestCase):
    account_list = account_list

    @classmethod
    #  类方法,执行类的时候自动执行类中的方法
    def setUpClass(cls) -> None:
        # 打开浏览器
        driver = get_driver()
        cls.login = LoginPage(driver)  # 初始化对象
        cls.index = IndexPage(driver)  # 初始化对象

    @ddt.data(*account_list)
    def test_login(self, data):
        username = data.get('username')  # 读取数据中的账号名
        password = data.get('password')  # 读取数据中的密码

        # 请求目标网址
        self.login.get(self.login.login_url)  # 请求的目标网址
        self.login.implicitly_wait()  #  使用隐式等待,全局生效

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
