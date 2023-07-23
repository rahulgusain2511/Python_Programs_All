d={}
flag=0
for i in range(5):
    name = input("Enter your name: ")
    email = input("Enter your emailid: ")
    d[name] = email
#print(d)
n = input("Enter any name to search an email: ")
for k in d:
    if(n == k):
        flag=1
        break
if flag==1:
    print(n,':',d[k])
else:
  print("Name not found.....")

