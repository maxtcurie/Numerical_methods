import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt


n=1000
x_list=np.random.rand(n)
y_list=np.random.rand(n)

count=0
for x,y in zip(x_list, y_list):
    if x**2.+y**2.<1:
        count=count+1

pi=4.*float(count)/float(n)

print('pi='+str(pi))


theta=np.arange(0,7,0.001)

plt.figure(figsize=(5,5),dpi=96) 
plt.scatter(x_list,y_list,alpha=0.2)
plt.plot(np.cos(theta),np.sin(theta))
plt.xlim(0,1.2)
plt.ylim(0,1.2)
plt.show()