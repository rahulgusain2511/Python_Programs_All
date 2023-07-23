#Reading Line by Line
def reading():
    file = open('Student.txt','r')
    doc=' '
    while(doc):
        doc = file.readline() #it also reads the newline character
        print(doc,end='')
            
reading()
