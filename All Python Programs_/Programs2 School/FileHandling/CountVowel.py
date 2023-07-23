#Counting Vowel

def vowel():
    file = open('STORY.txt','r')
    ch = ' '
    c=0
    while ch:
        ch = file.read(1)
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            c=c+1
    print('No of Vowels: ',c)


vowel()
