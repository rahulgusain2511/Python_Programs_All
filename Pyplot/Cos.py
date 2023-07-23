import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,.5)
y = np.cos(x)
y2 = np.sin(x+1)
plt.plot(x,y,'bo',linestyle='dashed')
plt.plot(x,y2,'g+',linestyle='dashdot')
plt.show()
