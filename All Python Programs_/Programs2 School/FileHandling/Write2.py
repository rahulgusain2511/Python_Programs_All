'''
write(string)
writelines(list)
'''
def Writing():
    file = open('abc.txt', 'a')
    st = input("Enter: ")
    file.write(st)
    file.close()

Writing()
