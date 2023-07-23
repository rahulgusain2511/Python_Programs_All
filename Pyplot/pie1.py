import matplotlib.pyplot as plt

plt.subplot(2,2,1)
v1 = [5,2,8,6,4,10]
plt.pie(v1)

plt.subplot(2,2,2)
v2 = [10,20,30,40,50]
plt.pie(v2)

plt.subplot(2,2,3)
plt.pie(v2)
#plt.axis('equal')
plt.show()
