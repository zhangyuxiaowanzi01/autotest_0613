import unittest


class DemoTestCase(unittest.TestCase):
    def test01(self):
        # 断言1和1相等
        self.assertEqual(1, 1, msg='断言失败')

    def test02(self):
        # 断言1和1不相等
        self.assertNotEqual(1, 1, msg='断言失败')
