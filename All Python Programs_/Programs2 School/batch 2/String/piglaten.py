a = input("Enter any li: ")
length = len(a)
a = a.lower()
for i in range(length):
    if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
        j=i
        break
#end of i loop
first = a[j:length]
last = a[0:j]+'ay'
py = first+last
print("Pyglatin String: ",py)
