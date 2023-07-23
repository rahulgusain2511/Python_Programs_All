import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,10)
y = [100,5,15,80,1000,780,456,56,1]
x2 = [1,1,2,2,2]
plt.subplot(3,2,1)
plt.plot(x2)
y = x**2
plt.subplot(3,2,2)
plt.plot(y)
plt.show()
