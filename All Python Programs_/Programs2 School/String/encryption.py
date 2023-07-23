#Encryption
#import string
s=''
st = input("Enter any word: ")
for i in st:
    if 't'<=i<='z':  
        a = ord(i) + 7
        a = a - 26
        #print(a)
        s = s + chr(a)#string.ascii_lowercase[a-1]
    else:
        a = ord(i)
        a = a + 7
        s = s + chr(a)
print(s)

'''
t 20
u 21
v 22
w 23
x 24
y 25
z 26
'''
