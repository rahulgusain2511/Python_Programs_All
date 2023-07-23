def Sort():
    lst=eval(input('enter a list'))
    leng=len(lst)
    for i in range(leng):
        for j in range(leng-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
        print('pass:',i+1,'\n',lst)
