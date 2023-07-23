st = input("enter any word: ")
l = len(st)
j = l-1
flag=1
for i in range(l//2):
    if(st[i] != st[j]):
        flag=0
        break;
    j= j-1
if(flag == 1):
    print('Palindrome')
else:
    print('Not a Palindrome')


