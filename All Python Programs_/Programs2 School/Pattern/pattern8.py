# question 19.1
a = 1
for i in range(0,5):  # rows
    for k in range(4,i,-1): #spaces
        print(end=" ")
    for j in range(0,2*i+1): #columns
        print("*",end="") 
    #end of j
    print()
#end of i
print("End")
