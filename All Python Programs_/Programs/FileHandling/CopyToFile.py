#
def copy():
    f1 = open('story.txt','r')
    f2 = open('dup.txt','w')

    sent=' '
    while sent:
        sent = f1.readline()
        sent = sent.upper()
        f2.write(sent)
    f1.close()
    f2.close()
    print('Content of duplicate file: ')
    f2 = open('dup.txt','r')
    sent = f2.read();
    print(sent)
    f2.close()


copy()
    
