#counting the
def countThe():
    file = open("story.txt",'r')
    ch = ' '
    c=0
    while ch:
        ch = file.readline()
        l = ch.split()
        if 'the' in l:
            c += 1
    print('No of the: ',c)

countThe()
