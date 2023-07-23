'''
CASE 1
A = []
for i in range(5):
    n = int(input('Enter any no: '))
    A.append(n)
print(A)

CASE 2
A = [0,0,0,0,0]
for i in range(5):
    A[i] = int(input('Enter any no: '))
print(A)

CASE 3
n = int(input('Enter List size: '))
A = [0]*n
for i in range(n):
    A[i] = int(input('Enter any no: '))
print(A)
'''
#List comprehension
# list = [expresssion loo_creating_list for(loop) condition]
A = []
for i in range(5):
    A.append(0)
print (A)
#------------------------
A = [0 for i in range(5)]    
print(A)

B = [i*2 for i in range(10)]
print(B)

C = [i for i in range(20) if i%2!=0]
print(C)









