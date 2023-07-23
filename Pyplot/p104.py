import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10,2)
y = np.arange(0,10,2)
plt.plot(x,y,'g',marker='+',markersize=15,markeredgecolor='r')
plt.grid(True)

plt.show()
