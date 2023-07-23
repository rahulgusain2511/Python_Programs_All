c=0
file=open('poem.txt','r')
st=file.readline()
while st:
    lst=st.split()
    c=c+lst.count('to')
    st=file.readline()
print('No of To:',C)
file.close()
