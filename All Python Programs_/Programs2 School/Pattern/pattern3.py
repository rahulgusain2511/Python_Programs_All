# question 17.4
a = 1
for i in range(1,6):  # rows
    for j in range(1,i+1): #columns
        print(a,end=" ")
        a=a+1
    print()
print("End")
