import unittest

"""
loader.discover(start_dir, pattern='test*.py')    通过目录路径加载
将start_dir目录下的，以test开始的所有py文件里面的测试方法加载
"""
loader = unittest.TestLoader()
suite = loader.discover('./test_cases', pattern='test_*.py')

# 执行器
unittest.TextTestRunner().run(suite)
