def interest(p,r=5,t=2):
    i = p*r*t/100
    return i

def main():
    p = int(input('Enter principle: '))
    r = float(input('Enter rate: '))
    t = int(input('Enter time: '))
    print(interest(p,r,t))
    print(interest(5000))

if __name__ == '__main__':
   main() 
