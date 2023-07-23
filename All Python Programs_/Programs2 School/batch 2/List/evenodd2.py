a = eval(input("enter any list: "))

e , od = 0,0
for i in range(len(a)):
    if a[i]%2 == 0:
        e +=1
    else:
        od +=1
print("NO of even: ",e)
print("NO of odd: ",od)
