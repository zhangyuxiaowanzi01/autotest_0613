import unittest


class DemoTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 所有test运行前执行一次
        print('setUpClass')

    def setUp(self) -> None:
        # 每个测试方法运行前执行
        print('setUp')

    def tearDown(self) -> None:
        # 每个测试方法运行完后执行
        print('teardown')

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    @classmethod
    def tearDownClass(cls) -> None:
        # 所有test运行完后执行一次
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main(verbosity=2)
