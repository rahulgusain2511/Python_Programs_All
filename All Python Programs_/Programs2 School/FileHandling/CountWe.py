#Printing line which starts with WE
def startWE():
    file = open("story.txt",'r')
    ch = ' '
    while ch:
        ch = file.readline()
        if ch[0:3]=='we ' or ch[0:3]=='WE ' or ch[0:3]=='We ':
            print(ch)

startWE()
