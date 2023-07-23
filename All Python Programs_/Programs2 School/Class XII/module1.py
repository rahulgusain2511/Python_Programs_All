#module
''' This module contain add, multiply & subtract functions'''

def add(a,b):
    ''' it take two number and perform addition'''
    return a+b
def multiply(a,b):
    ''' it take two number and perform product'''
    return a*b
def subtract(a,b):
    ''' it take two number and perform subtraction'''
    return a-b


def main():
    x = int(input("Enter any no: "))
    y = int(input("Enter any no: "))
    print("Sum: ",add(x, y))
    print("multiply: ",multiply(x, y))
    print("Difference: ",subtract(x, y))

if __name__=='__main__':
    main( )

