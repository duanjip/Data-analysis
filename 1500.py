# -*- coding = utf-8 -*-
# @time : 2021/10/25 14:44
# @Author : Jipeng Duan
# @File : 1500.py
# @Software: PyCharm


import matplotlib.pyplot as plt
import pandas as pd
import os

def IV_curve(file_path, save_path, show='False'):

    file_path = file_path

    folder = os.listdir(file_path)
    for file in folder:
        if "reverse" not in file and file.startswith("I_V-Sweep"):
            print(file)
            path1 = os.path.join(file_path, file)
            # print(path1)
            path2 = path1.replace(" (", "-reverse (")
            # print(path2)
            data1 = pd.read_csv(path1, skiprows=223)
            data2 = pd.read_csv(path2, skiprows=223)
            # print(data1)
            plt.rc('font', family='Times New Roman', size=16)
            plt.rcParams['xtick.direction'] = 'in'
            plt.rcParams['ytick.direction'] = 'in'

            plt.figure(figsize=[9, 6])
            plt.yscale('log')

            line1, = plt.plot(data1[" V1"], data1[" I1"], color='#845EC2', linewidth=1.5, linestyle='-',
                              label='SET')
            line2, = plt.plot(data2[" V1"], abs(data2[" I1"]), color='#D65DB1', linewidth=1.5, linestyle='-',
                              label='REVERSE')
            plt.legend(handles=[line1, line2], loc=4, framealpha=0)

            plt.title(file.replace('.csv', ''))

            plt.xlabel('Voltage (V)')
            plt.ylabel('Current (A)')

            if show == 'True':
                plt.show()
            else:
                plt.savefig(save_path + '\\' + file.replace('.csv', '.tif'), dpi=100)

def GV_curve(file_path, save_path, show='False'):

    file_path = file_path

    folder = os.listdir(file_path)
    for file in folder:
        if "reverse" not in file:
            print(file)
            # if file == "sample1 (cc=80uA).csv":
            path1 = os.path.join(file_path, file)
            # print(path1)
            path2 = file_path + file.replace(" (", "-reverse (")
            # print(path2)
            data1 = pd.read_csv(path1, skiprows=223)
            data2 = pd.read_csv(path2, skiprows=223)

            Conductance1 = abs(data1[" I1"] * 12900 / data1[" V1"])
            Conductance2 = abs(data2[" I1"] * 12900 / data2[" V1"])
            plt.rc('font', family='Times New Roman', size=16)
            plt.rcParams['xtick.direction'] = 'in'
            plt.rcParams['ytick.direction'] = 'in'

            plt.figure(figsize=[9, 6])
            # plt.yscale('log')

            line1, = plt.plot(data1[" V1"], Conductance1, color='#845EC2', linewidth=1.5, linestyle='-', marker='o',
                              markersize=7, label='SET')
            line2, = plt.plot(data2[" V1"], Conductance2, color='#D65DB1', linewidth=1.5, linestyle='-', marker='o',
                              markersize=7, label='REVERSE')
            # plt.legend(handles=[line1, line2], loc=1, framealpha=0)

            plt.title(file.replace('.csv', ''))

            # ax = plt.gca()
            # ax.yaxis.set_major_locator(plt.MultipleLocator(2))

            plt.xlabel('Voltage (V)')
            plt.ylabel('Conductance (2e\u00b2/h)')

            plt.grid(linestyle='--', axis='both')

            if show == 'Ture':
                plt.show()
            else:
                plt.savefig(save_path + '\\' + '[G]' + file.replace('.csv', '.tif'), dpi=100)

def RT_curve(file_path, save_path, show='False'):

    file_path = file_path

    folder = os.listdir(file_path)
    for file in folder:
        if file.startswith("R-t"):
            path = os.path.join(file_path, file)
            print(path)
            data = pd.read_csv(path, skiprows=224)
            plt.rc('font', family='Times New Roman', size=16)
            plt.rcParams['xtick.direction'] = 'in'
            plt.rcParams['ytick.direction'] = 'in'

            plt.figure(figsize=[11, 6])
            plt.yscale('log')

            line1, = plt.plot(data[" Time"], data[" R"], color='#845EC2', linewidth=1.5, linestyle='-', label='R')

            plt.legend(handles=[line1], loc=1)

            plt.title(file.replace('.csv', ''))

            plt.xlabel('Times (s)')
            plt.ylabel('R (Ω)')

            if show == 'True':
                plt.show()
            else:
                plt.savefig(save_path + '\\' + file.replace('.csv', '.tif'), dpi=100)

def IV_curve_GV_curve(file_path, save_path, show='False'):
    file_path = file_path

    folder = os.listdir(file_path)
    for file in folder:
        if "reverse" not in file and file.startswith("I_V-Sweep"):
            print(file)
            try:
                path1 = os.path.join(file_path, file)
                print(path1)
                path2 = path1.replace(" (", "-reverse (")
                print(path2)
                data1 = pd.read_csv(path1, skiprows=223)
                data2 = pd.read_csv(path2, skiprows=223)

            except FileNotFoundError as e:
                print(e)

                plt.rc('font', family='Times New Roman', size=16)
                plt.rcParams['xtick.direction'] = 'in'
                plt.rcParams['ytick.direction'] = 'in'

                plt.figure(figsize=[18, 6])

                plt.subplot(121)
                plt.yscale('log')

                line1, = plt.plot(data1[" V1"], data1[" I1"], color='#845EC2', linewidth=1.5, linestyle='-', label='SET')
                # line2, = plt.plot(data2[" V1"], abs(data2[" I1"]), color='#D65DB1', linewidth=1.5, linestyle='-', label='REVERSE')
                plt.legend(handles=[line1], loc=4, framealpha=0)

                plt.title(file.replace('.csv', ''))

                plt.xlabel('Voltage (V)')
                plt.ylabel('Current (A)')

                plt.subplot(122)

                Conductance1 = abs(data1[" I1"] * 12900 / data1[" V1"])
                # Conductance2 = abs(data2[" I1"] * 12900 / data2[" V1"])

                line3, = plt.plot(data1[" V1"], Conductance1, color='#845EC2', linewidth=1.5, linestyle='-', marker='o',
                                  markersize=7, label='SET')
                # line4, = plt.plot(data2[" V1"], Conductance2, color='#D65DB1', linewidth=1.5, linestyle='-', marker='o',
                #                   markersize=7, label='REVERSE')
                # plt.legend(handles=[line3, line4], loc=1, framealpha=0)

                plt.title(file.replace('.csv', '').replace('I_V-Sweep', 'G_V'))

                # ax = plt.gca()
                # ax.yaxis.set_major_locator(plt.MultipleLocator(2))

                plt.xlabel('Voltage (V)')
                plt.ylabel('Conductance (2e\u00b2/h)')

                plt.grid(linestyle='--', axis='both')

                if show == 'True':
                    plt.show()
                else:
                    plt.savefig(save_path + '\\' + file.replace('.csv', '.tif'), dpi=100)
            else:
                plt.rc('font', family='Times New Roman', size=16)
                plt.rcParams['xtick.direction'] = 'in'
                plt.rcParams['ytick.direction'] = 'in'

                plt.figure(figsize=[18, 6])

                plt.subplot(121)
                plt.yscale('log')

                line1, = plt.plot(data1[" V1"], data1[" I1"], color='#845EC2', linewidth=1.5, linestyle='-',
                                  label='SET')
                line2, = plt.plot(data2[" V1"], abs(data2[" I1"]), color='#D65DB1', linewidth=1.5, linestyle='-',
                                  label='REVERSE')
                plt.legend(handles=[line1, line2], loc=4, framealpha=0)

                plt.title(file.replace('.csv', ''))

                plt.xlabel('Voltage (V)')
                plt.ylabel('Current (A)')

                plt.subplot(122)

                Conductance1 = abs(data1[" I1"] * 12900 / data1[" V1"])
                Conductance2 = abs(data2[" I1"] * 12900 / data2[" V1"])

                line3, = plt.plot(data1[" V1"], Conductance1, color='#845EC2', linewidth=1.5, linestyle='-', marker='o',
                                  markersize=7, label='SET')
                line4, = plt.plot(data2[" V1"], Conductance2, color='#D65DB1', linewidth=1.5, linestyle='-', marker='o',
                                  markersize=7, label='REVERSE')
                # plt.legend(handles=[line3, line4], loc=1, framealpha=0)

                plt.title(file.replace('.csv', '').replace('I_V-Sweep', 'G_V'))

                # ax = plt.gca()
                # ax.yaxis.set_major_locator(plt.MultipleLocator(2))

                plt.xlabel('Voltage (V)')
                plt.ylabel('Conductance (2e\u00b2/h)')

                plt.grid(linestyle='--', axis='both')

                if show == 'True':
                    plt.show()
                else:
                    plt.savefig(save_path + '\\' + file.replace('.csv', '.tif'), dpi=100)

if __name__ == '__main__':
    IV_curve_GV_curve(r"G:\Experimental data\1500\2021.11.1-Ag-MoS2-Au", r"G:\Experimental data\1500\2021.11.2-figures", show="True")
    # IV_curve(r"G:\Experimental data\1500\2021.10.29-Ag-multi-layer", r"G:\Experimental data\1500\2021.10.29-figures", show="True")
    # RT_curve(r"G:\Experimenrtal data\1500\2021.11.1-Ag-MoS2-Au", r"G:\Experimental data\1500\2021.11.1-figures", show="Tru")