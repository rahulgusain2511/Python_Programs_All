'''
write(string)
writelines(list)
'''
def Writing():
    file = open('abc2.txt', 'w')
    lst = []
    for i in range(4):
        st = input("Enter Name: ")
        lst.append(st+'\n')
    file.writelines(lst)
    file.close()

Writing()
