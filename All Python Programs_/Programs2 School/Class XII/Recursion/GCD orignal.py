def GCD(dividend, divisior):
    r = dividend%divisior
    if(r == 0):
        return divisior
    else:
        
        return GCD(divisior, r)




def main():
    print('Enter any two numbers: ')
    a = int(input())
    b = int(input())

    if a>b:
        dividend = a
        divisior = b
    else:
        dividend = b
        divisior = a
    r = GCD(dividend, divisior)
    print("GCD: ",r)

if __name__ == '__main__':
    main()



