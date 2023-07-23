file = open('readingfun.txt','r')
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()
print(line1,line2,line3,line4)
word = line1.split() # it convert the line into words in the form of list
print(word)
print('the' in word)
