#Recording student details
def addStudent():
    file = open('Student.txt','a')  #

    rollno = input('Enter student Rollno: ')
    name = input('Enter student Name: ')
    age = input('Enter student Age: ')
    cla = input('Enter student Class: ')
    per = input('Enter student Percentage: ')
    file.write('\nRollno: '+rollno)
    file.write('\nName: '+name)
    file.write('\nClass: '+cla)
    file.write('\nAge: '+age)
    file.write('\nPercentage: '+per)
    file.write('\n-------------------')

    print('Record Add...')
    file.close()

def main():
    ch='y'
    while(ch=='y'):
        addStudent()
        ch = input('Do you wanna continue...(y/n) ')




if __name__=='__main__':
    main()
