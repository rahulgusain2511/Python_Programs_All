
st = input("Enter any word: ")
a = 0
c = 0
l = len(st)
for a in range(l):
    if st[a]=='a' or st[a]=='e' or st[a]=='i' or st[a]=='o' or st[a]=='u':
        c+=1
print("No of Vowels: ",c)
