# encoding=utf-8

import re
import os
import shutil
import uuid
from datetime import datetime

from number_map import get_9_9_Order, get_U_Order, get_Hui_Order


def rename_9_9_order(old_dir_path, specific_task_new_dir):
    """把图片名称批量重命名。
原名称为input_Cam001——input_Cam081。
现需要按照9行9列的格式，命名为
01_01,01_02……01_09;
……
……
……
09_01,09_02……09_09
"""
    specific_task_new_dir = os.path.join(specific_task_new_dir, "9_9_order")
    os.makedirs(specific_task_new_dir, exist_ok=True)
    filename_order_RegExp = re.compile(r"\d+")

    old_dir_files = os.listdir(old_dir_path)
    # 遍历文件进行重命名复制
    for single_old_file in old_dir_files:
        # 旧文件路径拼接
        old_file_name = os.path.join(old_dir_path, single_old_file)
        # 处理文件名中的数字,order为“次序”
        filename_old_order_reg_match_res = filename_order_RegExp.search(single_old_file)
        filename_old_order_reg_match_res_group = filename_old_order_reg_match_res.group()
        filename_old_order = int(filename_old_order_reg_match_res_group)
        # 拼接新文件路径+文件名
        new_fileName = get_9_9_Order(filename_old_order)+".png"
        new_file_name = os.path.join(specific_task_new_dir, new_fileName)
        # 复制
        shutil.copy2(old_file_name, new_file_name)

def U_order(old_dir_path, specific_task_new_dir):
    "U字形排序"
    specific_task_new_dir = os.path.join(specific_task_new_dir, "U_order")
    os.makedirs(specific_task_new_dir, exist_ok=True)
    filename_order_RegExp = re.compile(r"\d+")

    old_dir_files = os.listdir(old_dir_path)
    # 遍历文件进行重命名复制
    for single_old_file in old_dir_files:
        # 旧文件路径拼接
        old_file_name = os.path.join(old_dir_path, single_old_file)
        # 处理文件名中的数字,order为“次序”
        filename_old_order_reg_match_res = filename_order_RegExp.search(single_old_file)
        filename_old_order_reg_match_res_group = filename_old_order_reg_match_res.group()
        filename_old_order = int(filename_old_order_reg_match_res_group)
        # 拼接新文件路径+文件名
        u_name = get_U_Order(filename_old_order)
        if u_name != None:
            new_fileName = u_name +".png"
            new_file_name = os.path.join(specific_task_new_dir, new_fileName)
            # 复制
            shutil.copy2(old_file_name, new_file_name)
        else:
            continue

def Hui_order(old_dir_path, specific_task_new_dir):
    "回字形排序"
    specific_task_new_dir = os.path.join(specific_task_new_dir, "Hui_order")
    os.makedirs(specific_task_new_dir, exist_ok=True)
    filename_order_RegExp = re.compile(r"\d+")

    old_dir_files = os.listdir(old_dir_path)
    # 遍历文件进行重命名复制
    for single_old_file in old_dir_files:
        # 旧文件路径拼接
        old_file_name = os.path.join(old_dir_path, single_old_file)
        # 处理文件名中的数字,order为“次序”
        filename_old_order_reg_match_res = filename_order_RegExp.search(single_old_file)
        filename_old_order_reg_match_res_group = filename_old_order_reg_match_res.group()
        filename_old_order = int(filename_old_order_reg_match_res_group)
        # 拼接新文件路径+文件名
        u_name = get_Hui_Order(filename_old_order)
        new_fileName = u_name +".png"
        new_file_name = os.path.join(specific_task_new_dir, new_fileName)
        # 复制
        shutil.copy2(old_file_name, new_file_name)

def three_demands_handler(old_dir_path, specific_task_new_dir):
    # 处理需求三：排序，将001-081排序为9x9矩阵
    rename_9_9_order(old_dir_path, specific_task_new_dir)
    # U字型
    U_order(old_dir_path, specific_task_new_dir)
    # 回字形
    Hui_order(old_dir_path, specific_task_new_dir)

def main():
    # 测试序列路径，可以放入多目录进行批量处理
    to_do_rename_dir_list = [
        r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
        r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
        r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
        r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
        r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
    ]

    # 获取当前脚本所在的目录路径，并新建output目录，若目录存在则跳过
    current_directory = os.path.dirname(os.path.abspath(__file__))
    base_output_dir = os.path.join(current_directory, 'output')
    os.makedirs(base_output_dir, exist_ok=True)

    # 循环处理任务
    for old_dir_name in to_do_rename_dir_list:
        # old_dir_name: 待处理的目标目录，是完整路径
        now = datetime.now()
        formatted_date = now.strftime("%H_%M_%S")
        random_uuid = uuid.uuid4()
        # new_dir_name: 新生成的目录名字，是非完整路径名。避免批量处理多目录导致重名，使用时间、随机字符串命名，避免目录名重复
        new_dir_name = formatted_date + '-' + str(random_uuid)
        # 新建特定任务目录 ./output/时间戳命名任务/
        specific_task_new_dir = os.path.join(base_output_dir, new_dir_name)
        os.makedirs(specific_task_new_dir, exist_ok=True)
        # 处理
        three_demands_handler(old_dir_name, specific_task_new_dir)
        print("目录: {TARGET_DIR} 已处理至 {HANDLED_DIR}".format(TARGET_DIR=old_dir_name, HANDLED_DIR=specific_task_new_dir))

if __name__ == '__main__':
    main()