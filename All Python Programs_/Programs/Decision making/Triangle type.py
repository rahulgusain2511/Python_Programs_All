a = int(input('Enter First angle: '))
b = int(input('Enter Second angle: '))
c = int(input('Enter Third angle: '))
s = a+b+c
if s==180:
    if a>90 or b>90 or c>90:
        print('Obtuse triangle')
    elif a==90 or b==90 or c==90:
        print('Right triangle')
    else:
        print('Scalene triangle')
else:
    print('Triangle not possible')
