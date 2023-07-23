#Counting Vowel

def punc():
    file = open('Story.txt','r')
    ch = ' '
    sp, c, s = 0,0,0
    while ch:
        ch = file.read(1).lower()
        
        if ch==' ':
            sp=sp+1
        elif ch=='.':
            s += 1
        elif ch==',':
            c += 1        
    print('No of spaces: ',sp)
    print('No of comma: ',c)
    print('No of fullstop: ',s)

punc()
