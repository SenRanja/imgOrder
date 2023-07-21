# encoding=utf-8

# 全局变量，matrix_9_9，将数字按照 "01_01", "01_02", ..., "09_09" 的格式排列成 9x9 矩阵，排序使用索引进行读取
matrix_9_9 = []
for i in range(1, 10):
    for j in range(1, 10):
        # 使用 zfill() 方法确保输出的格式为两位数
        map_row_tmp = str(i).zfill(2)
        map_col_tmp = str(j).zfill(2)
        matrix_9_9.append("{map_row_tmp}_{map_col_tmp}".format(map_row_tmp=map_row_tmp, map_col_tmp=map_col_tmp))
# 注意matrix是从0开始计算，排序需要如下行代码 次序 - 1 操作
# print(matrix_9_9[81-1])

# 全局变量，U字形映射表
U_map = {
    3: 1,
    4: 2,
    5: 3,
    6: 4,
    7: 5,
    17: 6,
    16: 7,
    15: 8,
    14: 9,
    13: 10,
    12: 11,
    11: 12,
    19: 13,
    28: 14,
    29: 15,
    20: 16,
    21: 17,
    30: 18,
    31: 19,
    22: 20,
    23: 21,
    32: 22,
    33: 23,
    24: 24,
    25: 25,
    34: 26,
    35: 27,
    26: 28,
    27: 29,
    36: 30,
    45: 31,
    54: 32,
    53: 33,
    44: 34,
    43: 35,
    52: 36,
    51: 37,
    42: 38,
    41: 39,
    50: 40,
    49: 41,
    40: 42,
    39: 43,
    48: 44,
    47: 45,
    38: 46,
    37: 47,
    46: 48,
    55: 49,
    56: 50,
    57: 51,
    58: 52,
    59: 53,
    60: 54,
    61: 55,
    62: 56,
    63: 57,
    71: 58,
    70: 59,
    69: 60,
    68: 61,
    67: 62,
    66: 63,
    65: 64,
    75: 65,
    76: 66,
    77: 67,
    78: 68,
    79: 69,
}

# 全局变量，回字形映射表
Hui_map = {
    41: 1,
    40: 2,
    31: 3,
    32: 4,
    33: 5,
    42: 6,
    51: 7,
    50: 8,
    49: 9,
    48: 10,
    39: 11,
    30: 12,
    21: 13,
    22: 14,
    23: 15,
    24: 16,
    25: 17,
    34: 18,
    43: 19,
    52: 20,
    61: 21,
    60: 22,
    59: 23,
    58: 24,
    57: 25,
    56: 26,
    47: 27,
    38: 28,
    29: 29,
    20: 30,
    11: 31,
    12: 32,
    13: 33,
    14: 34,
    15: 35,
    16: 36,
    17: 37,
    26: 38,
    35: 39,
    44: 40,
    53: 41,
    62: 42,
    71: 43,
    70: 44,
    69: 45,
    68: 46,
    67: 47,
    66: 48,
    65: 49,
    64: 50,
    55: 51,
    46: 52,
    37: 53,
    28: 54,
    19: 55,
    10: 56,
    1: 57,
    2: 58,
    3: 59,
    4: 60,
    5: 61,
    6: 62,
    7: 63,
    8: 64,
    9: 65,
    18: 66,
    27: 67,
    36: 68,
    45: 69,
    54: 70,
    63: 71,
    72: 72,
    81: 73,
    80: 74,
    79: 75,
    78: 76,
    77: 77,
    76: 78,
    75: 79,
    74: 80,
    73: 81,
}

def get_9_9_Order(filename_old_order:int) -> str:
    '''1:01_01 2:01_02 3:01_03'''
    raw_data = filename_old_order
    return matrix_9_9[raw_data - 1]

def get_U_Order(filename_old_order:int) -> str:
    try:
        ret_filename = str(U_map[filename_old_order])
        return ret_filename
    except KeyError:
        return None

def get_Hui_Order(filename_old_order:int) -> str:
    ret_filename = str(Hui_map[filename_old_order])
    return ret_filename
