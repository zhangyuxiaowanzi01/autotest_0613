import pandas as pd

# TODO 文本格式数据 csv(,) tsv(\t), txt(自定义分隔符)
# 读取文件
# pd.read_csv(文件路径[， 分隔符='，'])
data = pd.read_csv('data/user_info.csv')
print(data.head())

data = pd.read_csv('data/lj_data.csv')
print(data.head())

# TODO excel数据
# pd.read_excel(文件路径[, sheet="第一个sheet"] )
data = pd.read_excel('data/sales.xlsx', sheet_name='2018')
# 输出前5行数据
print(data.head())


