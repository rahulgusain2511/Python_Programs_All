#Recording student details
def addStudent():
    file = open('Student.txt','a')
    rollno = input('Enter student Rollno: ')
    name = input('Enter student Name: ')
    age = input('Enter student Age: ')
    cla = input('Enter student Class: ')
    marks = input('Enter student Marks: ')
    record = rollno+'\t'+name+'\t\t'+cla+'\t'+age+'\t'+marks+'\n'
    file.write(record) 
    print('Record Add...')
    file.close()
    print('\n')
#-------------------showAll()----------
def showAll():
    print('\nRollno\tName\t\tClass\tAge\tMarks')
    file = open('Student.txt')
    record = file.read()
    print(record)
    file.close()
#--------------------searchStudent()-------
def searchStudent():
    flag=0
    file = open('Student.txt')
    n = input('Enter the rollno: ')
    record=file.readline()
    while(record):
        lst = record.split()
        if(n==lst[0]):
            flag=1
            break;
        record = file.readline()
    if(flag==1):
        print('Rollno\tName\tClass\tAge\tMarks')
        print(record)
    else:
        print('Student not found....')
    print('\n')
#-----------------------deleteStudent---------
def deleteStudent():
    import os
    flag=0
    file1 = open('Student.txt')
    file2 = open('duplicate.txt','w')
    n = input('Enter the rollno: ')
    record=file1.readline()
    while(record):
        lst = record.split()
        if(n!=lst[0]):
            file2.write(record)
        else:
            flag=1
        record = file1.readline()
    if(flag==1):
        print('Student found...')
    else:
        print('Student not found....')
    file1.close()
    file2.close()
    os.remove('Student.txt')
    os.rename('duplicate.txt','Student.txt')
    print('\n')

#--------------------modifyStudent-------
def modifyStudent():
    import os
    flag=0
    file1 = open('Student.txt')
    file2 = open('duplicate.txt','w')
    n = input('Enter the rollno whose record you want to modify: ')
    record=file1.readline()
    while(record):
        lst = record.split()
        if(n==lst[0]):
            rollno = input('Enter student Rollno: ')
            name = input('Enter student Name: ')
            age = input('Enter student Age: ')
            cla = input('Enter student Class: ')
            marks = input('Enter student Marks: ')
            record = rollno+'\t'+name+'\t\t'+cla+'\t'+age+'\t'+marks+'\n'
            file2.write(record)
            flag=1
        else:
            file2.write(record)
        record = file1.readline()
    if(flag==1):
        print('Student modified...')
    else:
        print('Student not found....')
    file1.close()
    file2.close()
    os.remove('Student.txt')
    os.rename('duplicate.txt','Student.txt')
    print('\n')
#-------------------main----------------
def main():
    ch='y'
    while(ch=='y'):
        print("1.Add Student")
        print("2.Show Student")
        print("3.Delete Student")
        print("4.Modify Student")
        print("5.Search Student")
        ch = int(input("Enter your choice: "))
        if(ch==1):
            addStudent()
        elif(ch==2):
            showAll()
        elif(ch==3):
            deleteStudent()
        elif(ch==4):
            modifyStudent()
        elif(ch==5):
            searchStudent()
        else:
            print("Wrong choice entered...")
        ch = input('Do you wanna continue...(y/n) ')



if __name__=='__main__':
    main()
