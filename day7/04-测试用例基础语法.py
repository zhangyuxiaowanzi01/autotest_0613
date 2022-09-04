import unittest


class DemoTestCase(unittest.TestCase):
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    def test03(self):
        print('test03')

    def mytest(self):
        # 如果方法名不是以test开始的，那么unittest在执行的时候，不会加载
        print('mytest')


if __name__ == '__main__':
    # 执行测试用例
    unittest.main(verbosity=2)
