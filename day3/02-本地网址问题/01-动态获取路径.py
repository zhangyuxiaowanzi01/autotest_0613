from selenium import webdriver
import os

# 打开浏览器， 请求目标网址-本地A.html
driver = webdriver.Chrome()

# 用程序来生成绝对路径
# __file__: 当前脚本的绝对路径
print(__file__)
# os.path.dirname(): 获取文件所在的目录
print(os.path.dirname(__file__))

# TODO 网址拼接
# 普通拼接
url1 = 'file://' + os.path.dirname(__file__) + 'html/demo.html'

# 建议拼接
# os.path.join(路径1， 路径2) 用来拼接路径
url2 = 'file://' + os.path.join(os.path.dirname(__file__), 'html/demo.html')


# driver.get('file:///Users/fine/teach/itsouce/autotest_0613/day3/%E4%BD%9C%E4%B8%9A/demo.html')
# driver.get(url1)
driver.get(url2)


# 总结
"""
1. 获取当前脚本的所在的绝对路径目录
__file__: 获取到脚本的绝对路径
os.path.dirname(): 获取绝对路径目录
os.path.join(): 绝对路径目录和本地要访问的页面进行拼接
"""
