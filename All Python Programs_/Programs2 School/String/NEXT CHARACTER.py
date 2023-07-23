st = input("Enter any sentence: ")
l = len(st)
print(st[0], end='')
for a in range(l):
    if(st[a] == ' '):
        print(st[a+1], end='')
