import unittest


class DemoTestCase(unittest.TestCase):
    @unittest.skip(reason='跳过测试的原因')
    def test01(self):
        print('test01')

    @unittest.skipIf(1 == 1, reason='条件成立跳过')
    def test02(self):
        print('test02')

    @unittest.skipUnless(1 == 2, reason='条件不成立跳过')
    def test03(self):
        print('test03')

    @unittest.expectedFailure
    def test04(self):
        self.assertEqual(1, 1, msg='预期失败')


if __name__ == '__main__':
    unittest.main(verbosity=2)
