import math
def volumeC(r,h):
    v = math.pi*r*r*h
    return v

def CSA(r, h):
    a = 2*math.pi*r*h
    return a

def main():
    print('Volume:',volumeC(5,10))
    print('CSA:',CSA(5,10))

if __name__=='__main__':
    main()
