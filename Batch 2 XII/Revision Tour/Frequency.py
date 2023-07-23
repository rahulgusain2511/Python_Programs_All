l = eval(input('Enter any 10 elements'))
n = int(input('Enter any number: '))
count=0
for i in range(len(l)):
    if l[i] == n:
        count +=1
print('Frequency: ',count)
