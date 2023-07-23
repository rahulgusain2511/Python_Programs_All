import tempconversion

t1 = int(input('Enter temp in C: '))
t2 = int(input('Enter temp in F: '))
print('Conversion C->F:',tempconversion.to_fah(t1))
print('Conversion F->C:',tempconversion.to_cent(t2))
