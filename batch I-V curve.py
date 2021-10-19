# -*- coding = utf-8 -*-
# @time : 2021/9/18 19:50
# @Author : Jipeng Duan
# @File : batch I-V curve.py
# @Software: PyCharm


import pandas as pd
import matplotlib.pyplot as plt
import os

path = r'G:\Experimental data\4200 semiconducter parameter analyzer\2021.10.8'
folder = os.listdir(path)
for file in folder:
    # print(file)
    if file.endswith('xls'):
        # print(file)
        file_path = os.path.join(path,file)

        data = pd.ExcelFile(file_path)

        data1 = pd.read_excel(file_path,sheet_name='Data')
        data2 = pd.read_excel(file_path,sheet_name=data.sheet_names[-1])

        plt.rc('font',family='Times New Roman',size=16)
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'

        plt.figure(figsize=[9,6])
        plt.yscale('log')

        line1, = plt.plot(data1.AV,abs(data1.AI),color='#845EC2',linewidth=1.5,linestyle='-',label='SET')
        line2, = plt.plot(data2.AV,abs(data2.AI),color='#D65DB1',linewidth=1.5,linestyle='-',label='REVERSE')
        plt.legend(handles=[line1,line2],loc=4,framealpha=0)

        plt.title(file.replace('.xls',''))

        plt.xlabel('Voltage (V)')
        plt.ylabel('Current (A)')

        plt.savefig(r'G:\Experimental data\4200 semiconducter parameter analyzer\2021.10.8-figures\\' + file.replace('.xls','.tif'),dpi=100)

        # plt.show()