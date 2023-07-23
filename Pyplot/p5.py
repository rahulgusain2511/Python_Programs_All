import matplotlib.pyplot as pyt

x1 = [1,2,3,4,5]
y1 = [10,20,30,40,50]

y2 = [12, 25,33,38,45]

pyt.plot(x1,y1,color='red',label='Line1',marker='^',markersize=20,markeredgecolor='b')


pyt.xlabel('Numbers')
pyt.ylabel('Values')
pyt.title('Line Graph')
pyt.grid(True)
pyt.legend()
pyt.show()
