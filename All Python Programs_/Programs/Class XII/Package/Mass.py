#MassCalculation
from MassConversion import *


print('1. Kg to Tonne')
print('2. Kg to Pound')
print('3. Pound to Kg')
print('4. Tonne to Kg')
print('5. Exit')
ch = int(input('Enter the choice: '))
wt = float(input('Enter the mass: '))
if ch==1:
        print('Mass in Tonne:',kgtotonne(wt))
elif ch==2:
        print('Mass in Pound:',kgtopound(wt))
elif ch==3:
        print('Mass in Kg:',poundtokg(wt))
elif ch==4:
        print('Mass in Kg:',tonnetokg(wt))
else:
        print('Wrong choice entered...')


