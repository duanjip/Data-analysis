# -*- coding = utf-8 -*-
# @time : 2021/9/18 20:39
# @Author : Jipeng Duan
# @File : G-V curve.py
# @Software: PyCharm


import pandas as pd
import matplotlib.pyplot as plt

file_path1 = r'G:\Experimental data\4200 semiconducter parameter analyzer\2021.9.25\7.2-set.xls'
# file_path2 = r'G:\Experimental data\4200 semiconducter parameter analysis\2021.9.25\7.1-reset.xls'
# file_path3 = r'G:\Experiment data\4200 semiconducter parameter analysis\2021.9.24\sample2-3-reset2-4-0.5mA.xls'

data = pd.ExcelFile(file_path1)
# print(data.sheet_names[-1])

data1 = pd.read_excel(file_path1,sheet_name='Data')
data2 = pd.read_excel(file_path1,sheet_name=data.sheet_names[-1])
# data3 = pd.read_excel(file_path1,sheet_name='Append2')

Conductance1 = abs(data1.AI*12900/data1.AV)
Conductance2 = abs(data2.AI*12900/data2.AV)
# Conductance3 = abs(data3.AI*12900/data3.AV)

plt.rc('font',family='Times New Roman',size=16)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

plt.figure(figsize=[9,6])
# plt.yscale('log')

line1, = plt.plot(data1.AV,Conductance1,color='#845EC2',linewidth=1.5,linestyle='-',marker='o',markersize=7,label='SET1')
line2, = plt.plot(data2.AV,Conductance2,color='#D65DB1',linewidth=1.5,linestyle='-',marker='s',markersize=7,label='SET2')
# line3, = plt.plot(data3.AV,Conductance3,color='#FF6F91',linewidth=1.5,linestyle='-',marker='v',markersize=7,label='SET3')
plt.legend(handles=[line1,line2],loc=1,framealpha=0)

plt.grid(linestyle='--')

plt.title("7.2-set")

# plt.xlim(0,0.65)
plt.xlabel('Voltage (V)')
plt.ylabel('Conductance (2e\u00b2/h)')

# plt.savefig(r'C:\Users\1594649073\Desktop\2021.9.25-figures\\' + '[G]' + "7.2-set.tif", dpi=600)

plt.show()