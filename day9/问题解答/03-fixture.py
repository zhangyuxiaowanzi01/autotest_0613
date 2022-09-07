import unittest


class Demo1TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    def setUp(self) -> None:
        print('setUp')

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    def tearDown(self) -> None:
        print('tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main()
