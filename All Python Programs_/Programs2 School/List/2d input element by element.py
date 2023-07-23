#input 1d element by element.
r = int(input('Enter no. of rows: '))
c = int(input('Enter no. of columns: '))

A = [[0 for col in range(c)] for row in range(r)]
B = [[0 for col in range(c)] for row in range(r)]
print(A)
#inputing
for i in range(r): # row
    for j in range(c): #columne
        A[i][j] = int(input("Enter any no. : "))

print(A)
print('Matrix: ')
for i in range(r): # row
    for j in range(c): #columne
        print(A[i][j], end=' ')
    print()
print('Transpose of A: ')
for i in range(r): # row
    for j in range(c): #columne
        B[j][i] = A[i][j]
    
for i in range(r): # row
    for j in range(c): #columne
        print(B[i][j], end=' ')
    print()

print('Left Diagonal Elements: ')
for i in range(r): # row
    for j in range(c): #columne
        if  i==j:
            print(A[i][j], end=' ')

print('Right Diagonal Elements: ')
for i in range(r): # row
    for j in range(c): #columne
        if  i+j==r-1:
            print(A[i][j], end=' ')
    
