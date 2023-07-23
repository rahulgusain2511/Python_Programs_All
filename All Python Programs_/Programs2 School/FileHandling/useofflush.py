def WITHOUTFLUSH():
    file = open('example.txt','w')
    file.write("Class XII\n")
    file.write("PYTHON\n")
    n = input()
    file.write(n)
    file.close()

WITHOUTFLUSH()
