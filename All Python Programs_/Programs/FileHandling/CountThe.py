#counting the
def countThe():
    file = open("story.txt",'r')
    ch = ' '
    c=0
    while ch:
        ch = file.readline().lower()
        l = ch.split()
        #print(l)
  #case1      c = c + l.count('the')

        for word in l:
            if word =='the':
                c += 1
    print('No of the: ',c)

countThe()
