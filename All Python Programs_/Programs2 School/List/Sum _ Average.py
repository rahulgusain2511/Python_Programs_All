n = eval(input("Enter any list"))
s = 0
length = len(n)
for i in range(0,length):
    s = s + n[i]
print("The sum of elements: ",s)
print("The Average: ",s/length)
