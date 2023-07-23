import time

a = int(input('Enter First No.: '))
b = int(input('Enter Second No.: '))
c = int(input('Enter Third No.: '))
t1 = time.time()
if a>b and a>c:
    print(a,' is Greatest')
if b>a and b>c:
    print(b,' is Greatest')
if c>a and c>b:
    print(c,' is Greatest')
t2 = time.time()
print('Execution Time: ',(t2-t1))
