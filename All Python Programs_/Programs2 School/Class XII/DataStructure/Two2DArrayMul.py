A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
C = [[0 for col in range(3)] for row in range(3)]

for i in range(3):
    s = 0
    for j in range(3):
        for k in range(3):
             s = s + A[i][k]*B[k][j]
        C[i][j] = s
        s=0

for row in range(3):
    for col in range(3):
        print(C[row][col], end=' ')
    print()
