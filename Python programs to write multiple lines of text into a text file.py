def write():
    f=open("daynote.txt",'w')
    while True:
        line=imput("enter Line:")
        f.write(line)
        choice=input("Are there more lines(Y/N):")
        if choice =='N':
            break
    f.close()    
