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
    # 普通执行方式
    # 会把当前模块中的所有测试用例方法都收集执行
    # unittest.main()

    # TODO suite测试套件
    # 创建suite对象
    suite = unittest.TestSuite()

    # TODO addTest()
    # 收集测试方法，收集方法的顺序，就是执行的顺序
    suite.addTest(Demo1TestCase('test01'))
    suite.addTest(Demo2TestCase('test_a'))

    # TODO 执行器执行方式
    # 只执行套件中收集的测试用例方法
    # 创建执行器对象
    runner = unittest.TextTestRunner(verbosity=2)
    # 执行操作, 传入测试套件
    runner.run(suite)
