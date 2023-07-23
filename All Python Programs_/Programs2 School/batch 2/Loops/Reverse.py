#Reverse
rev = 0
n = int(input("Enter any number: "))
while(n>0):
    r = n%10
    rev = r + rev*10
    n = n//10
print("Reverse: ",rev)
