import unittest
from test_cases import test_demo1, test_demo2

# TODO loader对象第一种形式
"""
# 创建加载器对象
loader = unittest.TestLoader()
# 参数：测试类
loader1 = loader.loadTestsFromTestCase(test_demo1.Demo1TestCase)
loader2 = loader.loadTestsFromTestCase(test_demo2.Demo2TestCase)
"""

# TODO loader对象第二种形式

# 参数：测试类
loader1 = unittest.defaultTestLoader.loadTestsFromTestCase(test_demo1.Demo1TestCase)
loader2 = unittest.defaultTestLoader.loadTestsFromTestCase(test_demo2.Demo2TestCase)

# 创建套件对象，收集加载器对象
suite = unittest.TestSuite()
# 单个添加
# suite.addTest(loader1)
# suite.addTest(loader2)
# 批量添加
suite.addTests([loader2, loader1])

# 执行器执行
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
