#Mississippi
s = input("Enter any word: ")
c = input("Enter any character: ")
for i in s:
    if i == c:
        print(i.upper(),end='')
    else:
        print(i ,end='')
