
# 图片排序

### U字形排序

![](imgs/U字型.jpg)

### 回字形排序

![](imgs/回字型——需求二.jpg)

### 重命名排序

把图片名称批量重命名。
原名称为input_Cam001——input_Cam081。
现需要按照9行9列的格式，命名为
01_01,01_02……01_09;
……
……
……
09_01,09_02……09_09

# 使用方法

进入`main.py`，给**to_do_rename_dir_list**库列表变量赋值路径。如：

```python
to_do_rename_dir_list = [
    r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
    r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
    r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
    r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
    r'C:\Users\ranja\Desktop\我自己的git\img_filename_order\测试序列',
]
```

会在当前目录的`output`目录输出所需结果。