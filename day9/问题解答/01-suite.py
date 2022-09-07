# 收集要执行的测试用例方法- test开始的那些方法
import unittest
from test1_demo import Demo1TestCase
from test2_demo import Demo2TestCase


# 套件
suite = unittest.TestSuite()
suite.addTest(Demo1TestCase('test01'))
# suite.addTest(Demo1TestCase('test02'))

list1 = [Demo2TestCase('testa'), Demo2TestCase('testb')]
suite.addTests(list1)

# 执行
runner = unittest.TextTestRunner()
runner.run(suite)


