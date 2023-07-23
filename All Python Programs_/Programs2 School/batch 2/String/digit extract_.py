st = input("Enter any string: ")
n = int(input("enter any number: "))
d=0
for i in st:
    if i.isdigit():
        d = int(i)+d*10
add = d + n
print(n,'+',d,'=',add)
