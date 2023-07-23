lst = eval(input('Enter any list: '))
n = eval(input('Enter any value: '))
count=0
for i in lst:
    if i==n:
        count +=1
    #closing of if
#closing of i
print('Frequency of a number: ',count)
