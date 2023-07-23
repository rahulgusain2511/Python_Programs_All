def writedata():
    file = open('studentdata.txt','w')
    r = int(input('Enter your rollno:'))
    n = input('Enter your name:')
    g = input('Enter your Grade:')
    #data = str(r)+' ' + n +' '+ g+'\n'
    #file.write(data)

    file.write(str(r))
    file.write(n)
    file.write(g)
    file.close()


writedata()
