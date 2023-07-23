l = eval(input('Enter the list: '))
n = int(input('Enter any number: '))
flag=0
beg = 0
last = len(l) - 1
while beg <= last:
    mid = (beg+last)//2
    if n > l[mid]:
        beg= mid + 1
    elif n < l[mid]:
        last = mid - 1
    else:
        flag=1
        break;
if flag==1:
    print('Number present at',(mid+1),' position')
else:
    print('Number not present')
