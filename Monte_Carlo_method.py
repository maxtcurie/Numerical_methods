import numpy as np
import pandas as pd

n=1000
x_list=np.random.rand(n)
y_list=np.random.rand(n)

count=0
for x,y in zip(x_list, y_list):
    if x**2.+y**2.<1:
        count=count+1

pi=4.*float(count)/float(n)

print('pi='+str(pi))