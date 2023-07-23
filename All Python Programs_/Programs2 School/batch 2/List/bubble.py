a = eval(input("Enter any list: "))
length = len(a)
for i in range(length):
    for j in range(0,length-1-i):
        if (a[j]> a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
    #end of j loop
#end of i loop
print("Sorted Array:\n",a)
