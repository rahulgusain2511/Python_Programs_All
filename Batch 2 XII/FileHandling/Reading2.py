file = open('readingfun.txt','r')
content = file.read(10)
print(content)
content = file.read(10)
print(content)
content = file.read(1)
print(content)
#---------
file.seek(0) # it put the file pointer at the start of a file.
ch = ' '
while ch:
    ch = file.read(1)
    print(ch,end='')

file.seek(0)
content = file.read()
size = len(content)
print('Size :',size)

