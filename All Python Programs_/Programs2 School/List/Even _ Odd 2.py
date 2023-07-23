#Multiple  every even no by 2 and odd no by 3
n = eval(input("Enter any list: "))

length = len(n)
for i in range(0,length):
    if (n[i]%2 == 0):
        n[i] = n[i]*2
    else:
        n[i] = n[i]*3
print("The given list: \n",n)
