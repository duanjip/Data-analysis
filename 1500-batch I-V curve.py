# -*- coding = utf-8 -*-
# @time : 2021/9/28 20:13
# @Author : Jipeng Duan
# @File : 1500-batch I-V curve.py
# @Software: PyCharm


import matplotlib.pyplot as plt
import pandas as pd
import os

file_path = r"G:\Experimental data\1500\2021.10.13\\"

folder = os.listdir(file_path)
for file in folder:
    if "reverse" not in file:
        print(file)
    # if file == "photo":
        path1 = os.path.join(file_path,file)
        # print(path1)
        path2 = file_path + file.replace(" (","-reverse (")
        # print(path2)
        data1 = pd.read_csv(path1,skiprows=223)
        data2 = pd.read_csv(path2,skiprows=223)
        # print(data1)
        plt.rc('font', family='Times New Roman', size=16)
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'

        plt.figure(figsize=[9, 6])
        plt.yscale('log')

        line1, = plt.plot(data1[" V1"], data1[" I1"], color='#845EC2', linewidth=1.5, linestyle='-', label='SET')
        line2, = plt.plot(data2[" V1"], abs(data2[" I1"]), color='#D65DB1', linewidth=1.5, linestyle='-', label='REVERSE')
        plt.legend(handles=[line1, line2], loc=4, framealpha=0)

        plt.title(file.replace('.csv', ''))

        plt.xlabel('Voltage (V)')
        plt.ylabel('Current (A)')

        # plt.savefig(r'G:\Experimental data\1500\2021.10.13-figures\\' + file.replace('.csv','.tif'),dpi=100)

        plt.show()