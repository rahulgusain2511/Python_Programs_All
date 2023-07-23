#Reading Line by Line using for loop
def reading():
    file = open('Student.txt','r')
    print(file)
    c = 0
    for doc in file:
        print(doc,end='')
        c = c+1
    print('\nNo of Line: ',c)
reading()
