import matplotlib.pyplot

x = [1,2,3,4]
y1 = [80,55,70,60]

y2 = [50,20,33,75]
matplotlib.pyplot.plot(x,y1,'red',label='Amit',linewidth=2,linestyle='dashed')
matplotlib.pyplot.plot(x,y2,'g',label='Mohit',linewidth=4,ls='dashdot')
matplotlib.pyplot.xlabel('Terms')
matplotlib.pyplot.ylabel('Marks')
matplotlib.pyplot.title('Result')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
