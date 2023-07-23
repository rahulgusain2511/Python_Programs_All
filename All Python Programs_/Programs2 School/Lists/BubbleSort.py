A = eval(input('Enter any list: '))
size = len(A)
for i in range(size):
    for j in range(size-1-i):
          if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
          #closing of if
     #closing of j
    #print('Pass: ',(i+1),"\n",A)
#closing of i
print("Sorted List: ")
print(A)
