def SUM(a):
    if a==1:
        return 1
    else:
        return a + SUM(a-1)

n = int(input('enter any number: '))
print('Sum: ',SUM(n))
