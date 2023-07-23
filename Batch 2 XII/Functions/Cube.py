def cube(n):
    return n*n*n

a = 5
b = 3
# a**3 + b**3
print(cube(a))

x = cube(a)
y = cube(b)  # variable
print('a**3 + b**3:',x+y)

print('Cube:',cube(5)) #literal
print('Cube:',cube(a+b)) #expression




