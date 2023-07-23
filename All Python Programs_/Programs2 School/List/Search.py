#Linear Search
li = [1,2,3,5,7,9,10,12,14,15,18,20,22,25,28,30,34,35,36,37,38,39,40]
flag = 0
num = int(input("Enter any no. (1-40) : "))
length = len(li)

for i in range(0,length):
    if(num == li[i]):
        flag=1
        break

if(flag == 1):
    print("No. found..")
else:
    print("No not found")
          
