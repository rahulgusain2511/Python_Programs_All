import matplotlib.pyplot as pyt

x1 = [1,2,3,4,5]
y1 = [10,20,30,40,50]
x2 = [11,12,13,14,15]
y2 = [11,22,35,40,25]

pyt.bar(x1, y1, color='green',label='2015')
pyt.bar(x2,y2, color='red', label='2018')

pyt.xlabel('Numbers')
pyt.ylabel('Values')
pyt.title('Bar Graph')
pyt.legend()
pyt.show()
