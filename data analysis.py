# -*- coding = utf-8 -*-
# @time : 2021/9/18 9:28
# @Author : Jipeng Duan
# @File : data analysis.py
# @Software: PyCharm


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**3

plt.xlim((-1,2))
plt.ylim((-2,3))

plt.xlabel('X')
plt.ylabel('Y')

line1, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='test1')
line2, =plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-',label='test2')
plt.legend(handles=[line1,line2],loc=0)

new_sticks = np.linspace(-2,2,11)
print(new_sticks)

plt.xticks(new_sticks)
plt.yticks([-1,0,1,2,3],
           ['level1','level2','level3','level4','level5'])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

x0 = 0.5
y0 = 2*x0 + 1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--',lw=2)
plt.annotate(r'y=2x+1',xy=(x0,y0),xytext=(+30,-30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->'))
plt.text(-1.5,1.5,r'this is text',fontdict={'size':10,'color':'y'})

plt.show()