#Q13
n = int(input("Enter any number: "))
for a in range(1, n+1):
    c = a**3
    if c%3 == 0:
        print(c, end=", ")
