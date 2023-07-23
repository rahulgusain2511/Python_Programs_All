#count 'to' from the file

c=0
file = open('poem.txt','r')
st = file.readline()
while st:
    lst = st.split()
    c = c + lst.count('to')
    st = file.readline()
print('No of TO:',c)
file.close()

'''
while st:
    lst = st.split()
    for w in lst:
        if w.upper() == 'TO':
            c = c + 1
    st = file.readline()
'''
