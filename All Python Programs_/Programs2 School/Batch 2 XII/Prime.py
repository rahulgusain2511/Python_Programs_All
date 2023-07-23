n = int(input('Enter any number: '))
c=0
for i in range(1,n//2+1):
    if n%i == 0:
        c +=1
if c == 1:
    print(n,'is Prime')
else:
    print(n,'is not Prime')
