import unittest
from HTMLTestRunner import HTMLTestRunner
import os

# 加载测试用例
suite = unittest.defaultTestLoader.discover('test_cases', 'test_*')

# 打开文件，用来写入测试结果，必须是.html结尾
# 准备要写入的文件的路径
file_path = os.path.join(os.path.abspath('report'), 'demo_test1.html')
f = open(file_path, 'wb')

# 执行器-使用生成测试报告模块下面的类
runner = HTMLTestRunner(
    title='测试报告标题',
    description='测试报告描述',
    tester='fine',
    stream=f,
    verbosity=2
)

runner.run(suite)

f.close()
