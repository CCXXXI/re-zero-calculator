# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:10:26 2020

@author: bruceye
"""
import math
import numpy as np
# from pandas import read_excel
from tools_excel import get_data

title_map = {'满级ATK': 'atk', '基础攻击': 'atk_bonus', '暴击几率': 'crit', '暴击伤害': 'crit_dam', '连击几率': 'combo',
             '连击伤害': 'combo_dam', '造成伤害': 'scaling', '忽视防御': 'dfc_ign', '吸取生命': 'vampire', 'AP技能伤害': 'ap',
             'SP技能伤害': 'sp', '必杀技伤害': 'ub'}


class ParaArray:
    def __init__(self, file_path=None, sheet_name=None):

        def rename(names):
            for i in range(len(names)):
                if names[i] in title_map:
                    names[i] = title_map[names[i]]

        if file_path is None or sheet_name is None:
            self.data = np.zeros((0, 0), dtype="double")
            self.row_index = {}
            self.col_index = {}
            return

        try:
            # data = read_excel(file_path, sheet_name=sheet_name).to_dict()
            data = get_data(file_path, sheet_name)
        except FileNotFoundError:
            print(file_path, '-', sheet_name, '未找到')
            raise
        else:
            print(file_path, '-', sheet_name, '已加载')

        title = list(data)
        row_names = list(data[title[0]].values())
        col_names = title[1:]
        row_index = self.get_index(row_names)
        col_index = self.get_index(col_names)

        self.data = np.zeros((len(row_names), len(col_names)), dtype="double")

        for x in col_names:
            for y in data[x]:
                if isinstance(data[x][y], float) or isinstance(data[x][y], int):
                    if not math.isnan(data[x][y]):
                        self.data[row_index[data[title[0]][y]]][col_index[x]] = data[x][y]

        rename(row_names)
        rename(col_names)
        self.row_index = self.get_index(row_names)
        self.col_index = self.get_index(col_names)

    @staticmethod
    def get_index(names):
        names = tuple(names)
        index = {}
        for i in range(len(names)):
            index[names[i]] = i
        return index

    def transpose(self):
        self.data = self.data.transpose()
        self.row_index, self.col_index = self.col_index, self.row_index

    def row_extend(self, names):
        data = np.concatenate((self.data, np.zeros((1, len(self.col_index)), dtype="double")))
        names_index = [self.row_index[x] if x in self.row_index else len(data) - 1 for x in names]
        self.data = data[np.array(names_index)]
        self.row_index = self.get_index(names)

    def col_extend(self, names):
        self.transpose()
        self.row_extend(names)
        self.transpose()

    def get_row(self, name):
        return self.data[self.row_index[name]][:]

    def get_col(self, name):
        return self.data.transpose()[self.col_index[name]]

    def value(self, x, y):
        return self.data[self.row_index[x]][self.col_index[y]]


if __name__ == '__main__':
    print('【当前环境】tools测试v3.0.1')
    test = ParaArray('心之器.xlsx', '心之器属性')
    print(test.data)
    print(test.col_index)
    print(test.row_index)
