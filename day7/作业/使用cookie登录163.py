"""
原理： 获取登录网站后的cookie， 然后再selenium操作网站的时候，将登录的cookie设置到当前cookie中

简单粗暴的办法： 把登录后的所有cookie直接获取，然后设置到selenium中

解决办法：

  		1. 用selenium登录网站，获取登录后的所有cookie。不退出
  		2. 用selenium打开这个网站，将获取到的cookie全部设置，刷新
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.163.com')

    def login(self):
        # 用selenium登录网站，获取登录后的所有cookie。不退出
        # 切换到登录的这个frame
        frame_element = self.driver.find_element(By.XPATH, '//iframe[contains(@id, "x-URS-iframe")]')
        self.driver.switch_to.frame(frame_element)

        # 定位账号输入框，输入账号
        time.sleep(2)
        self.driver.find_element(By.NAME, 'email').send_keys('itsourcetest')
        # 定位密码输入框，输入密码
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('Itsource123.')
        # 定位登录按钮，  点击登录
        time.sleep(2)
        self.driver.find_element(By.ID, 'dologin').click()

        # 获取所有cookie
        time.sleep(2)
        print(self.driver.get_cookies())

    def cookie_login(self):
        # 用selenium打开这个网站，将获取到的cookie全部设置，刷新
        # 准备cookie
        cookies = [{'domain': '.163.com', 'httpOnly': False, 'name': '_ntes_nuid', 'path': '/', 'secure': False,
                    'value': 'd99f11f1d8ffb807fb3c04e9446533c0'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'mail_host', 'path': '/', 'secure': False,
                    'value': 'mail.163.com'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'mail_uid', 'path': '/', 'secure': False,
                    'value': 'itsourcetest@163.com'},
                   {'domain': 'mail.163.com', 'httpOnly': False, 'name': 'Coremail.sid', 'path': '/', 'secure': False,
                    'value': 'uAfiECsufzolLqiCCGuuImfLEXQteXSu'},
                   {'domain': 'mail.163.com', 'expiry': 1696818171, 'httpOnly': False, 'name': 'face', 'path': '/',
                    'secure': False, 'value': 'js6'},
                   {'domain': 'mail.163.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False,
                    'value': 'AEC20255E81B0FE5A3A4238161F6D8CC'},
                   {'domain': '.163.com', 'expiry': 1693794171, 'httpOnly': False, 'name': 'P_INFO', 'path': '/',
                    'secure': False,
                    'value': 'itsourcetest@163.com|1662258171|0|mail163|00&99|sic&1662257373&mail163#sic&510100#10#0#0|&0|mail163|itsourcetest@163.com'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'mail_upx', 'path': '/', 'secure': False,
                    'value': 't4bj.mail.163.com|t3bj.mail.163.com|t3bj.mail.163.com|t4bj.mail.163.com'},
                   {'domain': '.mail.163.com', 'expiry': 1693794171, 'httpOnly': False, 'name': 'MAIL_PINFO',
                    'path': '/', 'secure': False,
                    'value': 'itsourcetest@163.com|1662258171|0|mail163|00&99|sic&1662257373&mail163#sic&510100#10#0#0|&0|mail163|itsourcetest@163.com'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'MAIL_SINFO', 'path': '/', 'secure': False,
                    'value': '1662258171|0|3&80##|itsourcetest'},
                   {'domain': '.mail.163.com', 'httpOnly': True, 'name': 'MAIL_SESS', 'path': '/', 'secure': False,
                    'value': 'ewtzss1JsUpElZZdHwIdhgzn37MS1Go9vQwQ.GUJc26fHglxHydKU4v8mfoT7nQxh6sHxScKQWy.OURr2NKvphT6TUryX1lLarcrQ1Qny.Pi3SbOjghhBWBT1.eMTCXvPR5vQ9ELHptqHkYlEcossU50MOvUI56lwgcewsps3L5OKbGaEAYdi53T16B2x8zb6McW7thXn_N14'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'cm_last_info', 'path': '/', 'secure': False,
                    'value': 'dT1pdHNvdXJjZXRlc3QlNDAxNjMuY29tJmQ9aHR0cHMlM0ElMkYlMkZtYWlsLjE2My5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRHVBZmlFQ3N1ZnpvbExxaUNDR3V1SW1mTEVYUXRlWFN1JnM9dUFmaUVDc3Vmem9sTHFpQ0NHdXVJbWZMRVhRdGVYU3UmaD1odHRwcyUzQSUyRiUyRm1haWwuMTYzLmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNEdUFmaUVDc3Vmem9sTHFpQ0NHdXVJbWZMRVhRdGVYU3Umdz1odHRwcyUzQSUyRiUyRm1haWwuMTYzLmNvbSZsPS0xJnQ9LTEmYXM9dHJ1ZQ=='},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'Coremail', 'path': '/', 'secure': False,
                    'value': '42fe330271426%uAfiECsufzolLqiCCGuuImfLEXQteXSu%g5a43.mail.163.com'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'secu_info', 'path': '/', 'secure': False,
                    'value': '1'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'mail_upx_nf', 'path': '/', 'secure': False,
                    'value': ''},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'mail_idc', 'path': '/', 'secure': False,
                    'value': '""'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'MAIL_ENTRY_CS', 'path': '/', 'secure': False,
                    'value': '19f553bebc55777d71e2e4799dbef822'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'df', 'path': '/', 'secure': False,
                    'value': 'mail163_letter'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'mail_style', 'path': '/', 'secure': False,
                    'value': 'js6'},
                   {'domain': '.163.com', 'httpOnly': True, 'name': 'NTES_SESS', 'path': '/', 'secure': False,
                    'value': 'ewtzss1JsUpElZZdHwIdhgzn37MS1Go9vQwQ.GUJc26fHglxHydKU4v8mfoT7nQxh6sHxScKQWy.OURr2NKvphT6TUryX1lLarcrQ1Qny.Pi3SbOjghhBWBT1.eMTCXvPR5vQ9ELHptqHkYlEcossU50MOvUI56lwgcewsps3L5OKbGaEAYdi53T16B2x8zb6McW7thXn_N14'},
                   {'domain': '.163.com', 'expiry': 1696818171, 'httpOnly': False, 'name': 'nts_mail_user', 'path': '/',
                    'secure': False, 'value': 'itsourcetest@163.com:-1:1'},
                   {'domain': '.mail.163.com', 'expiry': 1693794171, 'httpOnly': False, 'name': 'MAIL_SDID',
                    'path': '/', 'secure': False, 'value': '882576462447050752'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'MAIL_ENTRY_INFO', 'path': '/',
                    'secure': False,
                    'value': '1|0|mail163|mail163_letter|222.210.10.79|5d57422748aeae137979b3c58ab9ab36_v1|'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'mail_entry_sess', 'path': '/',
                    'secure': False,
                    'value': '65eaa3b6bf5a71157fde38fda6cef278bef9f70eb7621ce9baf0671fe237197ad2b731c0cf0c39daf584819684bd21ba4c46dd5cb5063f8d19059811c9bba080910df7516150fed618238f2dcf73c6662ba0d01a3ff3b096579b3e315cb7cdcfde6c153df93e9601171f340b57a54e9e658edf902e2cfccdfb7babf4fbb31f0e0019157265d34e324e7ef7fd01297b6bcc0dcd8ace4762c968f01d6224f089ffdadfe0fbb7dce51871b02eae0b1d0c05f3e1b496dae4ef80ef80367ed46a3947'},
                   {'domain': '.163.com', 'httpOnly': False, 'name': 'S_INFO', 'path': '/', 'secure': False,
                    'value': '1662258171|0|3&80##|itsourcetest'},
                   {'domain': '.mail.163.com', 'httpOnly': False, 'name': 'starttime', 'path': '/', 'secure': False,
                    'value': ''},
                   {'domain': '.163.com', 'expiry': 1693794171, 'httpOnly': False, 'name': 'NTES_P_UTID', 'path': '/',
                    'sameSite': 'None', 'secure': True, 'value': 'mq8Jzr4SUsCZl5B9MkMuGCjVoaCoIBgI|1662258171'},
                   {'domain': 'mail.163.com', 'expiry': 1696818171, 'httpOnly': False, 'name': 'locale', 'path': '/',
                    'secure': False, 'value': ''},
                   {'domain': 'mail.163.com', 'httpOnly': False, 'name': 'stats_session_id', 'path': '/',
                    'secure': False, 'value': '1e2c5112-f45f-4c07-823d-f3ddc3d26d7c'}]

        # 设置cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # 刷新浏览器
        self.driver.refresh()

    def quit(self):
        time.sleep(10)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.login()  # 获取登录之后的所有cookie
    case.cookie_login()  # 打开网址，使用cookie免登录
    case.quit()