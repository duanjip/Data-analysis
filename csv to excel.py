# -*- coding = utf-8 -*-
# @time : 2021/9/28 20:46
# @Author : Jipeng Duan
# @File : csv to excel.py
# @Software: PyCharm


import pandas as pd
import os

file_path = r"C:\Users\1594649073\Desktop\test\\"

folder = os.listdir(file_path)
for file in folder:
    path = os.path.join(file_path,file)

    csv = pd.read_csv(path, sep="\t", encoding='utf-8')
    csv.to_excel(r"C:\Users\1594649073\Desktop\1\\" + file.replace('.csv','.xlsx'), sheet_name='data')