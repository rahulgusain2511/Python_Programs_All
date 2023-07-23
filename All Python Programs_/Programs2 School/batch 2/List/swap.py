a = eval(input("enter any List: "))
length = len(a)
if length%2 == 0:
    end=length
else:
    end = length-1
i=0
while i<end:
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp
    i = i + 2
print(a)

#range(0,len(a),2)

