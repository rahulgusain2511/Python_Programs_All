import matplotlib.pyplot as plt
import numpy as np
a = [5,10,15,8,20]
b = [1,12,18,25,10]
x = np.arange(len(a))

plt.bar(x,a,width=.3)
plt.bar(x+0.3, b, width=0.3,color='r')
#limits
#plt.xlim(<min>,<max>)
plt.xlim(-10,10)
#marker
plt.plot(x,a,'y^',markersize=10)
plt.plot(x+0.25,b,'b^',markersize=10)
plt.grid(True)
plt.show()
