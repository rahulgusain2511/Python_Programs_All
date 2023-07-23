# question
a = 1
for i in range(0,3):  # rows
    for k in range(2,i,-1): #spaces
        print(end=" ")
    for j in range(0,2*i+1): #columns
        print("*",end="") 
    #end of j
    print()
#end of i
for i in range(1,-1,-1):  # rows
    for k in range(2,i,-1): #spaces
        print(end=" ")
    for j in range(0,2*i+1): #columns
        print("*",end="") 
    #end of j
    print()
#end of i
print("End")
