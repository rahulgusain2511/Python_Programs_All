import math

a = int(input('Enter the first side: '))
b = int(input('Enter the second side: '))
c = int(input('Enter the third side: '))

p = a+b+c
s = p/2
v = s*(s-a)*(s-b)*(s-c)

ar = math.sqrt(v)

print('Area of Triangle: ',ar)
print('Perimeter of Triangle: ',p)


