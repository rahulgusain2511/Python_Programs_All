a=0
c=0
st=input('Enter any string: ')
for a in range(len(st)):
    if st[a].isspace():  #if st[a]==' '
        c+=1
print("No of spaces: ",c)
