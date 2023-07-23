#Count the sentence that start with M.
def countM():
    file = open('data.txt','r')
    ch ='  '
    c=0
    while ch:
        ch = file.readline()
        if ch[0:1]=='M' or ch[0:1]=='m':
            c+=1
    print('No. of sentences starts with M: ',c)

countM()
        
