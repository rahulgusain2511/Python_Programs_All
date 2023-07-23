# plt.bar(<x - seq>, <y-seq>, color=<name/seq>, width=<value/seq>)
import matplotlib.pyplot as plt

name = ['Ajay','Aman','Abhi','Hitesh']
y = [35,45,28,10]
plt.bar(name,y,.3,color='r')
plt.show()
