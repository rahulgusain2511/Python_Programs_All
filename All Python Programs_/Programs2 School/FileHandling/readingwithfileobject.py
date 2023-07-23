def CountEmp():
    file = open('employee.txt')
    st=file.readline()
    while st:
        lst = st.split(':')
        if 20000< lst[2] <40000:
            print(st)
        st=file.readline()
    file.close()

def CopyFile():
    filename = input('Enter text file name: ')
    filename = filename+'.txt'
    filer = open(filename)
    filename = input('Enter text file name: ')
    filename = filename+'.txt'
    filew = open(filename,'w')
    for line in filer:
        filew.write(line)
    filer.close()
    filew.close()

#file = open('b.txt')

try:
    f = open('abc.txt')
    print('Try part')
except FileNotFoundError:
    print('File not found')
    pass
finally:
    print('end')











    
