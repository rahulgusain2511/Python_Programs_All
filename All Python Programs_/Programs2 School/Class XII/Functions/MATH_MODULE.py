def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def rem(a,b):
    return a%b

def pow(a,b):
    r=1   #return a**b
    for i in range(b):
        r = a * r
    return r

def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

