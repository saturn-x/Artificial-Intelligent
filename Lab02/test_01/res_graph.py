import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from numpy.core.fromnumeric import ptp
from matplotlib.pyplot import MultipleLocator
tmp=''
with open('./tmp.txt') as f:
    tmp=f.readlines()
x=[]
y=[] # x,y元素个数N应相同
for i in range(len(tmp)):
    x.append(i)
for i in tmp:
    y.append(int(i))
plt.plot(x,y,c='red')
plt.yticks(np.linspace(min(y),max(y),20,endpoint=True)) 
plt.show()

