'''
P : N
Y : O
T : H
H : T
O : Y
N : P
'''
s = input("Enter any word: ")
l = len(s)
for i in range(l):
    print(s[i],' : ',s[l-1-i])
