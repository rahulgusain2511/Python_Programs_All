import matplotlib.pyplot as plt

subject = ['english','hindi','maths','sci','sst','fit']
col = ['red','green','yellow','orange','black','white']
v = [85,30,98,96,90,92]
plt.pie(v,labels=subject,autopct='%05.1f%%',colors=col)
plt.axis('on')
plt.show()

#%[flags][width].['precision]type%
