a = eval(input("enter any List: "))
i,j=0,len(a)-1
while i<j:
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    i +=1
    j -=1
print(a)                                                  

