# -*- coding = utf-8 -*-
# @time : 2021/9/18 10:58
# @Author : Jipeng Duan
# @File : I-V curve.py
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

# print(abs(data2.AV))

plt.rc('font',family='Times New Roman',size=16)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 16, 'style': 'normal'}

plt.figure(figsize=[9,6])
plt.yscale('log')

line1, = plt.plot(data1.AV,abs(data1.AI),color='#845EC2',linewidth=1.5,linestyle='-',label='SET')
line2, = plt.plot(data2.AV,abs(data2.AI),color='#D65DB1',linewidth=1.5,linestyle='-',label='RESET')
# line3, = plt.plot(data3.AV,abs(data3.AI),color='#FF6F91',linewidth=1.5,linestyle='-',label='SET3')
plt.legend(handles=[line1,line2],loc=4,framealpha=0)
# plt.xticks(fontproperties='Times New Roman',size=14)
# plt.yticks(fontproperties='Times New Roman',size=14)

plt.title("7.2-set")

# plt.ylim(10**-14,10**-3)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')

# plt.arrow(0,10**-6,1,0.1,width=0.000001)

plt.savefig(r'C:\Users\1594649073\Desktop\2021.9.25-figures\\' + "7.2-set.tif", dpi=600)

plt.show()