'''
1
2 3
4 5 6
7 8 9 10
'''
a = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(a, end=' ')
        a = a + 1
    print()

