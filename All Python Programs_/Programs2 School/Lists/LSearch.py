lst = eval(input('Enter any list: '))
n = eval(input('Enter any value: '))
flag = False
size = len(lst)

for i in range(size):
    if lst[i] == n:
        flag=True
        break #come out from the loop
    #closing of if
#closing of i
if flag:
    print('No. is Present at: ',(i+1))
else:
    print('No. not Present')
