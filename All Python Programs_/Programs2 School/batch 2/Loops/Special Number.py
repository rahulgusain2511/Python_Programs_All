#Special Number
f = 1
s = 0 
n = int(input("Enter any number: "))
save = n
while(n>0):
    r = n%10
    while(r>=1):
        f = f*r
        r -= 1
    s = s + f
    f=1
    n = n//10
if save==s:
    print("Special Number")
else:
    print("Not a Special Number")
