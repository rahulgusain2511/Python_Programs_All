import matplotlib.pyplot as plt
import numpy as np
a = range(50,60)

x = np.arange(10,15,0.5)
plt.xticks(x)
plt.bar(x,a,width=.25)

plt.grid(True)
plt.show()
