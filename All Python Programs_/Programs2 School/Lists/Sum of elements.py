#sum of elements
s=0
lst = eval(input('Enter the list: '))
l = len(lst)
'''
for i in lst:
   s = s+i
mean = s/l
print("Sum: ",s)
print('Mean: ',mean)
'''
for i in range(0,l):
   s = s+lst[i]
mean = s/l
print("Sum: ",s)
print('Mean: ',mean)
