import unittest
from HTMLTestRunner import HTMLTestRunner
import os

# 加载测试用例
suite = unittest.defaultTestLoader.discover('test_cases', 'test_*')

# 确定写入文件的路径
filepath = os.path.join(os.path.abspath('report'), 'demo_test2.html')

# 执行测试用例，写入文件
with open(filepath, 'wb') as f:
    # 创建执行器
    runner = HTMLTestRunner(
        title='测试报告标题',
        stream=f,
        verbosity=2
    )
    # 执行器执行
    runner.run(suite)
