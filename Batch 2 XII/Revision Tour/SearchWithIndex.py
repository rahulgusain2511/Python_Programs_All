l = eval(input('Enter the list: '))
n = int(input('Enter any number: '))
flag=0
for i in range(len(l)):
    if l[i] == n:
        flag=1
        break
if flag==1:
    print('Number present at',i,' index')
else:
    print('Number not present')
