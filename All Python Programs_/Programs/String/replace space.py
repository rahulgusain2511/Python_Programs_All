st = input('Enter any sentence: ')
newst=''
for i in st:
    if i==' ':
        newst += '_'
    else:
        newst += i
print(newst)
