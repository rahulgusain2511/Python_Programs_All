l=eval(input('enter'))
small=l[0]
for i in range(1,len(l)):
    if l[i]<=small:
        small=l[i]
print(small)        
