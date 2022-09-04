import os

import pandas as pd


class DataOperation:
    def __init__(self, path):
        self.data = pd.read_csv(path)

    def get_data_to_dict(self):
        # [{}, {}, {}, ...]
        return [self.data.loc[i].to_dict() for i in self.data.index.values]

    def get_data_to_list(self):
        #[[], [], [], ...]
        return self.data.values.tolist()


if __name__ == '__main__':
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(project_path, 'data/lj_data.csv')  #join 专门用来路径拼接

    data = DataOperation(path)
    print(data.get_data_to_list())