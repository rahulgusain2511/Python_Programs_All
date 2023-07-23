def cube(n):
    return n*n*n

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return 'Division not possible.'
    else:
        return a/b

def main():
    x = int(input('Enter any number: '))
    y = int(input('Enter any number: '))

    print('Sum:',sum(x,y))
    print('Multiplication:',mul(x,y))
    print('Division:',div(x,y))
    print('Subtraction:',sub(x,y))

if __name__ == '__main__':
    main()


