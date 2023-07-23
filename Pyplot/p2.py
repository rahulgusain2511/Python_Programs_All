import matplotlib.pyplot as pyt

x1 = [1,2,3,4,5]
y1 = [10,20,30,40,50]

y2 = [12, 25,33,38,45]

pyt.plot(x1,y1,label='Line1')
pyt.plot(x1,y2, label='Line2')

pyt.xlabel('Numbers')
pyt.ylabel('Values')
pyt.title('Line Graph')
pyt.legend()
pyt.show()
