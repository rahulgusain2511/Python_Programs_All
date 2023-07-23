a =  int(input('Enter first Number:'))
b =  int(input('Enter second Number:'))
c=0
try:
    c = a/b
except:
    print('Number cannot divided by zero')
finally:
    print(c)
    
