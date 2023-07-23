#print those sentences which starts with 'we'

file = open('poem.txt','r')
st = file.readline()
while st:
    word = st[0:3].upper()
    if word == 'WE ':
        print(st,end='')
    st = file.readline()
file.close()
