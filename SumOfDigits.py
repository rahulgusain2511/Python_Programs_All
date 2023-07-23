n=int(input('enter no'))
sum=0
r=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10

print(sum)
