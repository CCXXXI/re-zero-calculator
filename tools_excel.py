import xlrd
from math import nan


def get_data(file_path, sheet_name):
    data = xlrd.open_workbook(file_path)
    table = data.sheet_by_name(sheet_name)
    cols_num = table.ncols
    rtn = dict()
    for cols_idx in range(cols_num):
        col = table.col_values(cols_idx)
        key, temp = col[0], col[1:]
        value = dict()
        for idx, content in enumerate(temp):
            value[idx] = content if content else nan
        rtn[key] = value
    return rtn


if __name__ == '__main__':
    print('【当前环境】tools_excel测试v3.0.0')
    test = get_data('心之器.xlsx', '心之器属性')
    print(test)
