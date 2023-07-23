#Q11
c=0
n = int(input("Enter any 6 or more digit number: "))
d = int(input("Enter any digit: "))
while n>0:
    if n%10 == d:
        c +=1
    n = n//10
    #end of loop
if c==0:
    print("Digit not found...")
else:
    print("No of occurence: ",c)
#end of program
