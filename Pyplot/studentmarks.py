import matplotlib.pyplot as plt
import numpy as np

s1 = [82,95,78,70,95]
s2 = [65,75,80,85,90]
x1 = np.arange(1,6,1)
sub = ['maths','phy','chem','eng','comp']

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.bar(x1,s1,width=.3)
plt.bar(x1+.3,s2,width=0.3)
plt.xticks(x1, sub)
#plt.savefig('result.pdf')
plt.savefig('C:\\Users\\User\\Pictures\\result.png')
plt.show()
