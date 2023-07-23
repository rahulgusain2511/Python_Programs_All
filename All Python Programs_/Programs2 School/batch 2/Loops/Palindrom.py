#Palindrom
rev = 0
n = int(input("Enter any number: "))
save = n
while(n>0):
    r = n%10
    rev = r + rev*10
    n = n//10
if save==rev:
    print("No. is Palindrom")
else:
    print("NO is not Palindrom")
