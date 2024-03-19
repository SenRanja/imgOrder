# encoding=utf-8

import re
import os
from openpyxl import load_workbook
from openpyxl import Workbook

def parseTxt(content) -> list:
    data = re.findall("     (\d{5,6}) bits", content)
    return data


def convert2excel(txt) -> list:
    single_row = [txt]
    sum = 0
    with open(txt_dir+txt) as f:
        content = f.read()
        data = parseTxt(content)
        for single_num in data:
            sum = sum + int(single_num)
        single_row.extend(data)
        single_row.append(sum)
    return single_row




# 全局变量
txt_dir = "./SRTE_testdata/36组数据/"
outputdir = "./SRTE_testdata/generateExcels/"
excelDir = "result.xlsx"

def main():

    wb = Workbook()
    my_sheet = wb.active

    data = []
    txts = os.listdir(txt_dir)
    for txt in txts:
        ret_single_row_list = convert2excel(txt)
        data.append(ret_single_row_list)
    # 行添加
    # for single_row in data:
    #     my_sheet.append(single_row)

    # 列添加
    columns = list(zip(*data))
    for column in columns:
        my_sheet.append(column)

    wb.save(outputdir+excelDir)

if __name__ == '__main__':
    main()