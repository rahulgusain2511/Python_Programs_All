s = 'PYTHON'
print("Through string: ")
for i in s:
    print(i,end='_')

l = len(s) # it finds the length of the string
print("\nThrough index: ")
for i in range(l):
    print(s[i], end='_')
