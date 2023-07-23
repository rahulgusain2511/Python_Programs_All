lst = eval(input('Enter any list: '))
e,od=0,0
for i in lst:
    if i%2 == 0:
        e = e + i
    else:
        od = od + i
    #closing of if
#closing of i
print('Sum of Even elements: ',e)
print('Sum of odd elements: ',od)
