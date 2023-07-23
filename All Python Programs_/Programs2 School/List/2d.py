l = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        print(l[i][j], end=' ')
    #end of j
    print()
        
print('Diagonal Elements: ')
for i in range(3):
    for j in range(3):
        if i==j:
            print(l[i][j], end=' ')
    #end of j

print('Right Diagonal Elements: ')
for i in range(3):
    for j in range(3):
        if i+j == 2:
            print(l[i][j], end=' ')
    #end of j

