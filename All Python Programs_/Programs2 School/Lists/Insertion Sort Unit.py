#INSERTION SORT
A = eval(input('Enter any List: '))
size = len(A)

for i in range(size):
    temp = A[i]
    t = A[i]%10
    j = i-1
    while j>=0 and t < A[j]%10:
        A[j+1] = A[j]
        j -= 1
    #end of while
    A[j+1] = temp
    print("Pass: ",(i+1),A)
#end of for
print('Sorted: ')
print(A)
