def WITHFLUSH():
    file = open('example.txt','w')
    file.write("Class XII\n")
    file.write("PYTHON\n")
    file.flush()
    n = input()
    file.write(n)
    file.close()

WITHFLUSH()
