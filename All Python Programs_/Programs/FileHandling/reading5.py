#Reading in the form of LIST
def reading():
    file = open('Student.txt','r')
    doc= file.readlines() #in the forem of list
    print(doc)
    print('No. of lines: ',len(doc))

    for st in doc:
        print(st,end='')
reading()
