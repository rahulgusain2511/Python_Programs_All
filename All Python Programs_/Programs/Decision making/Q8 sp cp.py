#Q8
sp = int(input("Enter the selling price: "))
cp = int(input("Enter the cost price: "))
if sp>cp:
    p = sp - cp
    per = (p/cp)*100
    print('Profit percent: ',per, end='%')
elif sp<cp:
    l = cp - sp
    per = (l/cp)*100
    print("Loss percent: ",per, end='%')
else:
    print('No loss no gain')
