def Smallest():
    l=eval(input('enter the list'))
    small=l[0]
    for i in range(1,len(l)):
                    if l[i]<=small:
                        small=l[i]
    print('smallest:',small)
                  
