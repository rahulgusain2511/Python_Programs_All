def display4():
    print('Hello i am display 4')
    print("Bye Bye from display 4")

def display3():
    print('Hello i am display 3')
    display4()
    print("Bye Bye from display 3")
    
def display2():
    print('Hello i am display 2')
    display3()
    print("Bye Bye from display 2")

def display1():
    a = 10
    print('Hello i am display 1')
    display2()
    print("Bye Bye from display 1")

##################
def main():
    display1()
    print("END")

if __name__=='__main__':
    main()
