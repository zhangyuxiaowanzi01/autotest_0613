"""
数据操作类， 用来读取测试数据
"""
import pandas as pd
import os
from pprint import pprint


class DataOperation:
    def __init__(self, filename, file_type='csv', sheet_name=0):
        # 读取文件
        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_path, 'data', filename)

        if file_type == 'csv':
            self.data = pd.read_csv(file_path)
        else:
            self.data = pd.read_excel(file_path, sheet_name)

    def get_data_to_list(self):
        # 提取数据转化为列表
        return self.data.values.tolist()

    def get_data_to_dict(self):
        # 提取数据转化为字典
        return [self.data.iloc[i].to_dict() for i in self.data.index.values]


if __name__ == '__main__':
    data = DataOperation('user_info.csv')
    pprint(data.get_data_to_list())
    pprint(data.get_data_to_dict())
