n = int(input('Enter any number: '))
s=0
save = n
while n>0:
    r = n%10
    s = s +r
    n = n//10
print('Sum of digits: ',s)
    
