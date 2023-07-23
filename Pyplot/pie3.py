import matplotlib.pyplot as plt

subject = ['english','hindi','maths','sci','sst','fit']
v = [85,30,98,96,90,92]
col = ['r','g','b','k','c','y']
space = [0.13,0,0,0,0,0]
plt.pie(v,labels=subject,autopct='%06.1f%%', colors=col, explode=space)
plt.title('RESULT') 

#plt.axis('on')
plt.show()


