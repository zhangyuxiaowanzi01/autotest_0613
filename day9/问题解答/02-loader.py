# 将测试用例方法，通过多种方式，添加到套件中
import unittest
import test1_demo
import test2_demo

# 加载器
loader = unittest.TestLoader()
suite1 = loader.loadTestsFromModule(test1_demo)
suite2 = loader.loadTestsFromModule(test2_demo)

# 套件 suite
suite = unittest.TestSuite()
suite.addTest(suite1)
suite.addTest(suite2)

# 执行
runner = unittest.TextTestRunner()
runner.run(suite)
