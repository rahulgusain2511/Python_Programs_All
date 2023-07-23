def palidrome(n):
    rev=0
    save=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==save:
        print(save,'is palidrome')
    else:
        print(save,'is not palidrome')
