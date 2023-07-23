A = []
for i in range(3):
    row = []
    for j in range(3):
        n = int(input('Enter any number: '))
        row.append(n)
    A.append(row)
print(A)

print('Matrix: ')
for i in range(3):
    for j in range(3):
        print(A[i][j], end=' ')
    print()
