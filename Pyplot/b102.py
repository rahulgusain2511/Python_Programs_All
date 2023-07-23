# plt.bar(<x - seq>, <y-seq>, color=<name/seq>, width=<value/seq>)
import matplotlib.pyplot as plt

name = ['Ajay','Aman','Abhi','Hitesh']
y = [35,45,28,10]
w = [.4,.7,.2,.5]
c = ['r','g','b','y']
plt.bar(name,y,width=w,color=c)
plt.xlabel('Student-Names')
plt.ylabel('Marks')
plt.title('Student Marks distribution')
plt.show()
