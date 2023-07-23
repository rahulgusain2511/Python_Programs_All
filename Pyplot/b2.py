import matplotlib.pyplot as pyt

x1 = ['AMAN','MOHIT','RAHUL','MANU']
y1 = [80,50,78,55]
#y1 = [x for x in range(100)]

w = [.2,.4,.6,.8]
pyt.bar(x1,y1, width=w, color=['r','b','k','c'])
pyt.xlabel('Names')
pyt.ylabel('Marks')
pyt.show()
