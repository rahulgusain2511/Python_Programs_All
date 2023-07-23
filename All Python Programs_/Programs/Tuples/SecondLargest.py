tup = eval(input('Enter the tuple: '))
m = max(tup)
sm = 0
for i in tup:
    if sm<i and i<m:  #i<sm<m
        sm = i
print('Second Largest No: ',sm)
