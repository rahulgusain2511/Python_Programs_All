import time
start = time.time()
def sumNatural(n):
    fs = time.time()
    s = 0
    for i in range(1,n):
        s = s + i
    es = time.time()
    print('Function time',round(es-fs,2),'Seconds')
    return s
n = int(input('Enter any no: '))
print(sumNatural(n))
end = time.time()
print(round(end-start,2),'Seconds')
