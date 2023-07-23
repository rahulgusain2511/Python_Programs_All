
with open('abc2.txt','r') a 
    for st in f:
        print(st,end='')
    f.seek(0)
    s=f.readline()
    print(s)

