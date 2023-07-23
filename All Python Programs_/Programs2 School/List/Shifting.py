#A[1,2,3,4,5,6,7] :  [5,6,7,4,1,2,3]
A = eval(input('Enter any list: '))
size = len(A)
if size%2 ==0:
    mid = size//2
else:
    mid = size//2 + 1
i=0
while i<size//2:
    temp = A[i]
    A[i] = A[mid+i]
    A[mid+i] = temp
    i+=1
print(A)
