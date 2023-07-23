#Area of Triangle

import math
print("Enter the Sides of a triangle: ")
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

s = (a+b+c)/2
area =math.sqrt(s*(s-a)*(s-b)*(s-c))

print('Area: ',area)
#ends
