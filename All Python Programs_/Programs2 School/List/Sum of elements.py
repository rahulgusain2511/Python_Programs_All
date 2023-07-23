lst =eval(list(input("Enter any list: ")))
leng = len(lst)
print (lst)

s=0
for a in range(leng):
    s = s + lst[a]
print("Sum: ",s)
avg = s/leng
print("Average: ",avg)

