#count vowels from the file

c=0
file = open('poem.txt','r')
ch = file.read(1)
while ch:
    if ch in 'aeiouAEIOU':
        c = c + 1
    ch = file.read(1)
print('No of vowels:',c)
file.close()


