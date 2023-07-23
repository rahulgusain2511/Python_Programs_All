# question 18.1
a = 1
for i in range(1,6):  # rows
    for j in range(5,i-1,-1): #columns
       print("*", end=" ") 
    #end of j
    print()
#end of i
print("End")
