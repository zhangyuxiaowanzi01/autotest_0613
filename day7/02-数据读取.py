# pandas读取数据
import pandas as pd
from pprint import pprint

# 打开数据文件
df = pd.read_csv('data/lj_data.csv')
# TODO df.loc   根据行、列的标签值查询
# df.loc[行标签，列标签].values
"""
print(df.loc[0, '区域'])
print(df.loc[1, '区域'])
print(df.loc[1, ['区域', '地址']].values)
print(df.loc[1].values)  # 获取行标签为1的数据

print('==================' * 4)
"""

# df.loc[[行标签1， 行标签2， ...], [列标签1， 列标签2, ...]]
"""
print(df.loc[[1, 3, 5, 8]]) # 获取行
print(df.loc[[1, 3, 5], ['区域', '标题', '价格']])
"""
# TODO df.iloc 根据行、列的数字位置查询，从零开始
# df.iloc[行索引，列索引]   获取单行
"""
print(df.iloc[1, 0])
print(df.iloc[1, [1, 2, 3]].values)

# df.iloc[[行索引1， 行索引2， ...], [列索引1， 列索引2, ...]] 获取多行多列
print(df.iloc[[1, 3, 5], [1, 3, 5]].values)
"""

# TODO 结果：列表数据类型  df.iloc[].values.tolist()
# [[], [], [], ...]
pprint(df.iloc[[1, 2, 3]].values.tolist())

# TODO 结果：字典数据类型  df.iloc[index].to_dict()
# [{}, {}, {}, ...]
# print(df.index.values)  # 获取数据的行索引


list1 = []
for i in df.index.values:
    list1.append(df.iloc[i].to_dict())

# 列表推导式
# list2 = [生成列表元素的表达式 生成列表元素个数的表达式]
list2 = [df.iloc[i].to_dict() for i in df.index.values]

print(list2[:2])
print(len(list2))
