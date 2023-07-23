#Reading a whole document
def reading():
    file = open('Student.txt','r')
    doc = file.read()
    print(doc)

reading()
