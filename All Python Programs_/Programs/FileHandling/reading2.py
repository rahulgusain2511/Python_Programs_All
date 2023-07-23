#Reading character by character
def reading():
    file = open('Student.txt','r')
    doc=' ' #this make doc with some inital value. 
    while(doc):
        doc = file.read(1)
        print(doc,end='')

reading()
