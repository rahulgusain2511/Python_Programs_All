# question 17.6
a = 1
for i in range(1,6):  # rows
    for j in range(1,i+1): #columns
        if((i+j)%2 == 0):
            print("1", end=" ")
        else:
            print("0", end=" ")
    #end of j
    print()
#end of i
print("End")
