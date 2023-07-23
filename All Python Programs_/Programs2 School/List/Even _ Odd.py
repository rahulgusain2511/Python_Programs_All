n = eval(input("Enter any list"))
ev = 0
od = 0
length = len(n)
for i in range(0,length):
    if (n[i]%2 == 0):
        ev = ev + 1
    else:
        od += 1
print("The number of even numbers: ",ev)
print("The number of odd numbers: ",od)
