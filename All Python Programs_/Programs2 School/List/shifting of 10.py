a=eval(input("enter list"))
l=len(a)
m=[]
i=0
while(i<l):
    if a[i]%10==0:
        m.append(a[i])
        a.remove(a[i])
    else:
        i +=1
    l = len(a)
a.extend(m)
print(a)
             
