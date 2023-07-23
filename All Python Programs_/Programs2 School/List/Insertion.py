A = eval(input('Enter any list: '))
size = len(A)
for i in range(size):
    temp = A[i]
    j = i-1
    while j>=0 and temp<A[j]:
        A[j+1] = A[j]
        j -=1
    #end of while
    A[j+1] = temp
    print('Pass : ',(i+1),A)
#end of i
