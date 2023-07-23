#series

s,k,f=0,1,1
n = int(input('Enter the range'))
x = int(input('Enter any number'))
for i in range(1,n+1):
    s = s + ((x**i)/i)*k
    k = k * -1
print('Sum of series: ',s)
