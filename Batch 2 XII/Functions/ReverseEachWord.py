def CapFL(st):
    st = ' '+st+' '
    i,j = 1, 0
    s=''
    l = len(st)
    while i<l:
        if st[i]==' ':
            k = i-1
            while k>=j:
                s = s + st[k]
                k = k -1
            j = i
        i = i+1
    return s

s = input('Enter any string: ')
print(CapFL(s))

