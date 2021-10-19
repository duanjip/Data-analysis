# -*- coding = utf-8 -*-
# @time : 2021/9/24 12:05
# @Author : Jipeng Duan
# @File : merge excel column.py
# @Software: PyCharm


import pandas as pd
import os

filename = r"C:\\Users\\1594649073\\Desktop\\columns.xlsx"
df = pd.read_excel(filename)
# col_name = df.columns.tolist()

path = r'G:\Experiment data\4200 semiconducter parameter analysis\2021.9.15 4200'
folder = os.listdir(path)
for file in folder:
    # print(file)
    if file.endswith('xls'):
        # print(file)
        file_path = os.path.join(path,file)
        data1 = pd.read_excel(file_path,sheet_name='Data')
        df.append(data1.AV)
        # col_name.append(data1.AV)
# df = df.reindex(columns=col_name)
df.to_excel("C:\\Users\\1594649073\\Desktop\\final.xlsx",index=False)