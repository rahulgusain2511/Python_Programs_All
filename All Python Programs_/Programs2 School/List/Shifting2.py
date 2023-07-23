#A[1,2,3,4,5,6,7] :  [7,1,2,3,4,5,6]
A = eval(input('Enter any list: '))
size = len(A)
temp = A[size-1]
i = size-2
while(i>=0):
    A[i+1] = A[i]
    i-=1
A[0] = temp
print(A)
    
