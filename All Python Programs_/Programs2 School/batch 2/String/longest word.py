st = input("enter any sentence: ")
st = st +' '
maxlen=0
maxword=''
sub=''
l = len(st)
for i in range(l):
    if st[i]!=' ':
        sub = sub+ st[i]
    else:
        l2 = len(sub)
        if l2>maxlen:
            maxlen = l2
            maxword = sub
        sub=''
print(maxword,maxlen)
    
    
