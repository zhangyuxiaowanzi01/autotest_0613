from common.base import Base, By


class LoginPage(Base):
    login_url = 'https://ecshop.test2.shopex123.com/user.php'

    def input_username(self, username):
        """
        接收用户名输入
        :param username: 用户名
        :return:
        """
        self.send_keys((By.NAME, 'username'), username)

    def input_password(self, password):
        """
        输入密码
        :param password: 用户密码
        :return:
        """
        self.send_keys((By.NAME, 'password'), password)

    def input_remember(self):
        """
        点击保存这次的登录信息
        :return:
        """
        self.click((By.ID, 'remember'))

    def input_submit(self):
        """
        点击登录操作
        :return:
        """
        self.click((By.NAME, 'submit'))
