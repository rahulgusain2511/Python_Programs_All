A=[[0 for col in range(3)] for row in range(3)]
for row in range(3):
    for col in range(3):
        A[row][col] = int(input('Enter any number: '))

for row in range(3):
    for col in range(3):
        print(A[row][col],end=' ')
    print()
#Sum of all elements
s=0
for row in range(3):
    for col in range(3):
        s = s + A[row][col]
print('Sum of Elements: ',s)

#Sum of rows
s=0
for row in range(3):
    for col in range(3):
        s = s + A[row][col]
    print('Sum of Row Elements: ',s)
    s=0
#Sum of Columns
s=0
for row in range(3):
    for col in range(3):
        s = s + A[col][row]
    print('Sum of Column Elements: ',s)
    s=0
#Sum of Left Diagonal 
s=0
for i in range(3):
    s = s + A[i][i]
print('Sum of Left Diagonal Elements: ',s)

#Sum of Right Diagonal 
s=0
for i in range(3):
    s = s + A[i][2-i]
print('Sum of Right Diagonal Elements: ',s)









