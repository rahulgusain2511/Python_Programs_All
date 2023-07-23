'''
if cond1:
    True
elif cond2:
    True
elif cond3:
    True
else:
    False  (Optional)
---------
if cond1:
    True
if cond2:
    True
if cond3:
    True
if cond4:
    True
    '''
#input any three no. and find out the greatest no.
import time

a = int(input('Enter First No.: '))
b = int(input('Enter Second No.: '))
c = int(input('Enter Third No.: '))
t1 = time.time()
if a>b and a>c:
    print(a,' is Greatest')
elif b>a and b>c:
    print(b,' is Greatest')
else:
    print(c,' is Greatest')
t2 = time.time()
print('Execution Time: ',(t2-t1))







