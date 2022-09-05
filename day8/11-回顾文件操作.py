# TODO 普通文件操作方式
# 打开文件
f = open('report/test01.txt', mode='w', encoding='utf8')
# 操作文件
f.write('test01')
# 关闭文件
f.close()

# TODO 上下文文件操作方式
with open('report/test02.txt', 'w', encoding='utf8') as f:
    # 文件操作，不需要关闭文件，这个代码块执行完毕后，会自动关闭文件资源句柄
    f.write('test02')
