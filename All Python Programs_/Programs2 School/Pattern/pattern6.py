# question 18.4
a = 1
for i in range(1,6):  # rows
    for j in range(5,i-1,-1): #columns
       print(j, end=" ") 
    #end of j
    print()
#end of i
print("End")
