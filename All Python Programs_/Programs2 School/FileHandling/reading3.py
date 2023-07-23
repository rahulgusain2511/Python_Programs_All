#Reading Line by Line
def reading():
    file = open('Student.txt','r')
    doc=' '
    while(doc):
        doc = file.readline()
        print(doc,end='')
            
reading()
