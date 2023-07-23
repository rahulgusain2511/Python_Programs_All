file=open('poem.txt','r')
st=" "
st=file.readline()
while st:
    if st[0] in 'wW':
        print(st,end=' ')
    st=file.readline()
file.close()
