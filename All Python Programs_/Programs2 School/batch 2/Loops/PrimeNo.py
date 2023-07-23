#Prime Number
c=0
n = int(input("Enter any number: "))
for a in range(1, (n//2)+1):
   if n%a == 0:
        c += 1
if c==1:
    print(n," is a Prime Number")
else:
    print(n," is not a Prime Number")
