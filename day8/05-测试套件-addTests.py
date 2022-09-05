import unittest


class Demo1TestCase(unittest.TestCase):
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')


class Demo2TestCase(unittest.TestCase):
    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')


if __name__ == '__main__':
    # TODO suite测试套件
    # 创建suite对象
    suite = unittest.TestSuite()

    # TODO addTests()
    # 收集 test01， test02， test_b
    # 执行顺序按照元素顺序执行
    tests = [
        Demo1TestCase('test01'),
        Demo2TestCase('test_b'),
        Demo1TestCase('test02')
    ]

    suite.addTests(tests)

    # runner
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
