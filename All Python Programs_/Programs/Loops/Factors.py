# Factors

n = int(input("enter any no: "))
for i in range(1,(n)//2+1):
    if n%i == 0:
        print(i, end=', ')
print(n,"\nEnd")

