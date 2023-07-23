def writedata():
    file = open('studentdata2.txt','a')
    r = input('Enter your rollno:')
    n = input('Enter your name:')
    g = input('Enter your Grade:')
    g = g+'\n'
    lst = [r,n,g]
    file.writelines(lst)
    file.close()

n = int(input('Enter the number of details to be enter: '))
for i in range(n):
    writedata()
print('End')
