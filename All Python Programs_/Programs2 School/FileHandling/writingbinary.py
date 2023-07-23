#Writing on a binary file
def writing():
    file = open("binary.dat",'a')
    st = input('Enter any thing: ')
    file.write(st)
    file.close()

writing()
