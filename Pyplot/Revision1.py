import matplotlib.pyplot as plt
import numpy as np
x = np.arange(4)
name = ['Rahul','Mayank','Mohit','Sandeep']
y1 = [99, 67, 45, 20]
y2 = [77,23,77,65]
plt.bar(x,y1,width=.25)
plt.bar(x+0.25,y2, width=0.25)
plt.xticks(x,name)
#plt.xlim(2,5)
plt.show()
