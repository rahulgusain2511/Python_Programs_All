def FLUSH():
    file = open('ABC.txt','w')
    file.write('hello')
    file.write('Bye')
    file.flush()
    file.write('hello')
    file.write('Bye')
    a = input()
    file.close()

FLUSH()
