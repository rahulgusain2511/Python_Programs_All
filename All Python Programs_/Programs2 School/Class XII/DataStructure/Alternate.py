def ALTER(L, R, C):
    if(C%2 == 0):
        for i in range(R):
            for j in range(0,C,2):
                print(L[i][j], end=' ')
    else:
        for i in range(R):
            for j in range(C):
                if (i+j)%2 == 0:
                    print(L[i][j], end=' ')


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
ALTER(L, R, C)

