def Heading():
    file = open('Student2.txt','a')
    file.write('Rollno\tName\tMarks\tClass\n')

def AddStudent():
    while True:
        r = input('Enter your Rollno: ')
        name = input('Enter your Name: ')
        marks = input('Enter your marks: ')
        cl = input('Enter your class:')
        details = r+'\t'+name+'\t'+marks+'\t'+cl+'\n'
        file.write(details)
        ch = input('Do you want to continue: (Y/N) ')
        if ch not in 'yY':
            break
    file.close() 

AddStudent()
        
        
