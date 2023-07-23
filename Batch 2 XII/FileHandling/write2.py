def writedata():
    file = open('studentdata.txt','a')
    r = int(input('Enter your rollno:'))
    n = input('Enter your name:')
    g = input('Enter your Grade:')
    data = str(r)+' ' + n +' '+ g+'\n' #converting a record into a string
    file.write(data)
    file.close()

n = int(input('Enter the number of details to be enter: '))
for i in range(n):
    writedata()
print('End')
