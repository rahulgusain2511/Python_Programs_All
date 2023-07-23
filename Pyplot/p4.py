import matplotlib.pyplot as pyt

x1 = [1,2,3,4,5]
y1 = [10,20,30,40,50]

y2 = [12, 25,33,38,45]

pyt.plot(x1,y1,color='black',label='Line1',linestyle='dashdot')
pyt.plot(x1,y2,color='green',label='Line2',linestyle='dotted')
pyt.plot(x1,[4,5,10,15,18],color='r',label='Line3',linestyle='dashed')
pyt.grid(True)

pyt.xlabel('Numbers')
pyt.ylabel('Values')
pyt.title('Line Graph')
pyt.legend()
pyt.show()
