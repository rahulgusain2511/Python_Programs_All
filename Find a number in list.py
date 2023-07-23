def Find():
    l=eval(input('enter any list'))
    n=int(input('enter any number'))
    flag=0
    beg=0
    last=len(l)-1#(L-one)
    while beg<=last:
        mid=(beg+last)//2
        if n>l[mid]:#L
            beg=mid+1#one
        elif n<l[mid]:#L
            last=mid-1#one
        else:
            flag=1#one
            break;
    if flag==1:#one
        print('number present at',(mid+1),'position')#one
    else:
        print('number not present')
