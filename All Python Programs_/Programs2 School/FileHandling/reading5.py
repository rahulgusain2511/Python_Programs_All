#Reading in the form of LIST
def reading():
    file = open('Student.txt','r')
    doc= file.readlines()
    print(doc)
    print('No. of lines: ',len(doc))

    for st in doc:
        print(st,end='')
reading()
