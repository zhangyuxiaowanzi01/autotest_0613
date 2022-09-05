import unittest
from test_cases import test_demo1, test_demo2

# loader.loadTestsFromModule(模块)
# 通过模块加载测试方法

default_loader = unittest.defaultTestLoader
loader1 = default_loader.loadTestsFromModule(test_demo1)
loader2 = default_loader.loadTestsFromModule(test_demo2)

# 测试套件
suite = unittest.TestSuite()
suite.addTests([loader2, loader1])

# 执行器
unittest.TextTestRunner().run(suite)
