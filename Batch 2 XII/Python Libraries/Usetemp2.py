from tempconversion import to_fah, to_cent, Freezing_F

#to include all the function from the module
#from tempconversion import *

#to create alias name
#import matplotlib as pt

t1 = int(input('Enter temp in C: '))
t2 = int(input('Enter temp in F: '))
print('Conversion C->F:',to_fah(t1))
print('Conversion F->C:',to_cent(t2))
