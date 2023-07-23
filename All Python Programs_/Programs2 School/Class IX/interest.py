p = float(input('Enter the Principle: '))
r = float(input('Enter the Rate: '))
t = float(input('Enter the duration: '))

i = (p*r*t)/100

amt = p + i
print('Interest: ',i)
print('Amount: ',amt)
