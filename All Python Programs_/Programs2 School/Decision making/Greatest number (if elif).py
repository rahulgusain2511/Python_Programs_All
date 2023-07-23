#Greatest number amoung the three numbers
#if elif

a = int(input("Enter First: "))
b = int(input("Enter Second: "))
c = int(input("Enter Third: "))
if a>b and a>c:
    print(a,' is greatest')
elif b>a and b>c:
    print(b,'is greatest')
elif c>a and c>b:
    print(c,'is greatest')
else:
    print('All are equal')

#ends
