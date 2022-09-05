import unittest
from test_cases import test_demo1, test_demo2

"""
# 参数： 名字，字符串类型
loader.loadTestsFromName(str)       通过测试模块名|类名|方法名加载 
  ○ 模块名 或者 包名.模块名
  ○ 模块名.类名
  ○ 模块名.类名.方法名
"""
# TODO 通过模块名加载测试方法
# loader = unittest.defaultTestLoader.loadTestsFromName('test_cases.test_demo1')

# TODO 通过类名加载测试方法
# loader1 = unittest.defaultTestLoader.loadTestsFromName('test_cases.test_demo1.Demo1TestCase')
# loader2 = unittest.defaultTestLoader.loadTestsFromName('test_cases.test_demo2.Demo2TestCase')

# TODO 通过方法名加载测试方法
loader1 = unittest.defaultTestLoader.loadTestsFromName('test_cases.test_demo1.Demo1TestCase.test01')
loader2 = unittest.defaultTestLoader.loadTestsFromName('test_cases.test_demo2.Demo2TestCase.test_b')

# 创建测试套件
suite = unittest.TestSuite()
# suite.addTest(loader)
suite.addTests([loader1, loader2])

# 执行器执行测试
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
