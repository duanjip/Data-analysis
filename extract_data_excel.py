# -*- coding = utf-8 -*-
# @time : 2021/9/1 8:20
# @Author : Jipeng Duan
# @File : extract_data_excel.py
# @Software: PyCharm


import pandas as pd

date = pd.read_excel(r"C:\Users\1594649073\\Desktop\date\LTP-LTD@2.xls")
dateframe = date.loc[date['序号']=="C",["Time","G"]]
dateframe.to_excel(r"C:\Users\1594649073\Desktop\date\2.xlsx")