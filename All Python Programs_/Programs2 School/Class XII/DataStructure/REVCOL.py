def REVCOL(L, R, C):
    for i in range(R):
        for j in range(C//2):
            L[i][j], L[i][C-1-j] = L[i][C-1-j], L[i][j]

R = int(input('Enter no. of rows: '))
C = int(input('Enter no. of columns: '))
L=[[0 for col in range(C)] for row in range(R)]
for row in range(R):
    for col in range(C):
        L[row][col] = int(input('Enter any number: '))
for row in range(R):
    for col in range(C):
        print(L[row][col], end=' ')
    print()
    
REVCOL(L, R, C)
print('--------------------------')

for row in range(R):
    for col in range(C):
        print(L[row][col], end=' ')
    print()
