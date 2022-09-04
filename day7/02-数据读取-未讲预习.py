import pandas as pd
from pprint import pprint

# 打开csv文件
data = pd.read_csv('data/lj_data.csv')

# data.loc[行标签, 列标签]
# print(data.loc[0])
# print(data.loc[0, '地址'])

# data.loc[[行标签， 行标签], [列标签， 列标签]]
# print(data.loc[[0, 1, 2, 6]])
# print(data.loc[[0, 1, 2, 6], ['标题', '户型', '价格']])

# dt.iloc i:index
# pt.iloc[行索引， 列索引]
# print(data.iloc[1])
# print(data.iloc[1, 0])

# df.iloc[[行索引1， 行索引2， ...], [列索引1， 列索引2, ...]]
# print(data.iloc[[1, 2, 3], [1, 2, 3, 4]])

# 将pd读取出的数据转化为列表字典　　　［｛｝，｛｝，｛｝］
# list1 = []
# for i in data.index.values:
#     list1.append(data.loc[i].to_dict())

# 列表推导式
list1 = [data.loc[i].to_dict() for i in data.index.values]
pprint(list1[:2])

#　将ｐｄ读取出的数据转化为列表列表　　［［］，［］，［］］
# pprint(data.iloc[[0, 1, 2, 3]].values.tolist())




