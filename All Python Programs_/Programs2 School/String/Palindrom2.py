st = input("Enter any word: ")
a=0
flag=1
l = len(st)
for a in range(0,l//2):
    if st[a] != st[l-1-a]:
        flag=0
        break;
if flag==1:
    print("Palindrom")
else:
    print("Not a Palindrom")
