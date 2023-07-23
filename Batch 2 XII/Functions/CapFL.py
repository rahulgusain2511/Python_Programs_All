def CapFL(st):
    l = len(st)
    i=1
    newst=st[0].upper()
    while i<l-1:
        if st[i]==' ':
            newst = newst+st[i-1].upper()
            newst = newst+' '
            newst = newst+st[i+1].upper()
            i = i+1
        elif st[i+1] != ' ' :
            newst = newst+st[i]
        i = i+1
    newst = newst + st[l-1].upper()
    return newst

s = input('Enter any string: ')
print(CapFL(s))

