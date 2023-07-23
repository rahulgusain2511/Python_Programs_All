import os, sys
#--------------AddStudent------
def addStudent():
    file = open('SGRR.txt','a')
    r = input('Enter your rollno:')
    name = input('Enter your name:')
    cl = input('Enter your class:')
    m = input('Enter your marks:')
    data = r+'\t'+name+'\t'+cl+'\t'+m+'\n'
    file.write(data)
    print('\nStudent added')
    file.close()
    
#--------------ShowAll------------
def displayAll():
    file = open('SGRR.txt','r')
    print('Rollno\tName\tClass\tMarks')
    data = ' '
    while data:
        data = file.readline()
        print(data,end='')        
    file.close()

#---------------search()---------
def search():
    flag = False
    file = open('SGRR.txt','r')
    r = input('Enter rollno:')
    data = ' '
    while data:
        data = file.readline()
        lst = data.split('\t')
        if r == lst[0]:  #rollno index
            print('Rollno\tName\tClass\tMarks')
            print(data)
            flag=True
            break
    if not flag:
        sys.stderr.write('Record not found')
    file.close()
#----------------Delete------------
def delete(): 
    flag=False
    orignal = open('SGRR.txt','r')
    dup = open('dup.txt','w')
    r = input('Enter rollno:')
    data = ' '
    while data:
        data = orignal.readline()
        lst = data.split('\t')
        if r == lst[0]:  #rollno index
            flag=True
        else:
            dup.write(data)
            
    if flag:
        sys.stderr.write('Record Deleted...')
    else:
        sys.stderr.write('Record not found\n')
    orignal.close()
    dup.close()
    os.remove('SGRR.txt')
    os.rename('dup.txt', 'SGRR.txt')

#----------------Modify------------
def modify(): 
    flag=False
    orignal = open('SGRR.txt','r')
    dup = open('dup.txt','w')
    r = input('Enter rollno:')
    data = ' '
    while data:
        data = orignal.readline()
        lst = data.split('\t')
        if r == lst[0]:  #rollno index
            ro = input('Enter your rollno:')
            name = input('Enter your name:')
            cl = input('Enter your class:')
            m = input('Enter your marks:')
            data = ro+'\t'+name+'\t'+cl+'\t'+m+'\n'
            dup.write(data)
            flag=True
        else:
            dup.write(data)
            
    if flag:
        sys.stderr.write('Record updated...')
    else:
        sys.stderr.write('Record not found\n')
    orignal.close()
    dup.close()
    os.remove('SGRR.txt')
    os.rename('dup.txt', 'SGRR.txt')
    
#-------------------Main----------
def main():
    while(1):
        print('\n----------------')
        print('1. Add Student')
        print('2. Show All Student')
        print('3. Delete Student')
        print('4. Modify Student')
        print('5. Search Student')
        print('6. Exit')
        ch = int(input('Enter your choice: '))
        if ch==1:
            addStudent()
        elif ch==2:
            displayAll()
        elif ch==3:
            delete()
        elif ch==4:
            modify()
        elif ch==5:
            search()
        else:
            break

if __name__=='__main__':
    main()
