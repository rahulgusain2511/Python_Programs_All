import numpy as np
import matplotlib.pyplot as plt
n_groups=5
men_means = (22,30,33,30,26)
women_means = (25,32,30,35,29)
y_pos = np.arange(len(men_means))

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.bar(2*y_pos,women_means,color='g',linewidth=3,label="Women's score")
plt.bar(2*y_pos+1,men_means,color='b',linewidth=3,label="Men's score")

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by Person')
plt.legend()
plt.show()
